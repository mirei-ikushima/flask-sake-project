import os
from flask import render_template, redirect, url_for, abort
from flask_login import login_required, current_user
from werkzeug.utils import secure_filename
from app import create_app
from . import main
from .forms import NewBottleForm
from ..models import User, Bottle


@main.route('/')
def index():
    return render_template('index.html')


@main.route('/collection/<name>/<int:page>')
@main.route('/collection/<name>/', defaults={"page": 1})
def collection(name, page):
    user = User.query.filter_by(username=name).first()

    if user is None:
        abort(404)

    title = user.username

    bottles = Bottle.query.filter_by(user_id=user.id).paginate(page=page, per_page=15, error_out=False)

    user_total = User.bottles_total(name)

    return render_template('collection.html',
                           user=user,
                           user_total=user_total,
                           title=title,
                           bottles=bottles)


@main.route('/collections/<int:page>')
@main.route('/collections/', defaults={"page": 1})
def all_collections(page):
    users = User.users_with_bottles().paginate(page=page, per_page=10, error_out=False)

    if users is None:
        return redirect(url_for('main.collection',
                                name=current_user.username))

    total_collections = Bottle.total_collections()

    return render_template('gallery.html',
                           users=users,
                           total_num=total_collections,
                           title='Browse Collections')


@main.route('/collection/newbottle', methods=['GET', 'POST'])
@login_required
def update_collection():
    bottle_form = NewBottleForm()

    if bottle_form.validate_on_submit():

        if bottle_form.photo.data:
            f = bottle_form.photo.data
            fname = secure_filename(f.filename)
            f.save(os.path.join(create_app().config['UPLOADS_FOLDER'], fname))

            new_bottle = Bottle(owner=current_user.username,
                                label=bottle_form.label.data,
                                identifier=bottle_form.identifier.data,
                                photo=fname,
                                category=bottle_form.category.data,
                                maker=bottle_form.maker.data,
                                status=bottle_form.status.data,
                                region=bottle_form.region.data,
                                price=bottle_form.price.data,
                                notes=bottle_form.notes.data,
                                user_id=current_user.id
                                )
            new_bottle.save_bottle()

        else:
            new_bottle = Bottle(owner=current_user.username,
                                label=bottle_form.label.data,
                                identifier=bottle_form.identifier.data,
                                photo=None,
                                category=bottle_form.category.data,
                                maker=bottle_form.maker.data,
                                status=bottle_form.status.data,
                                region=bottle_form.region.data,
                                price=bottle_form.price.data,
                                notes=bottle_form.notes.data,
                                user_id=current_user.id
                                )
            new_bottle.save_bottle()

        return redirect(url_for('main.collection',
                                name=current_user.username))

    return render_template('new_bottle.html',
                           title='New Bottle',
                           bottle_form=bottle_form,
                           originalbottle=None)


@main.route('/collection/delete/<int:id>', methods=['POST'])
@login_required
def delete_bottle(id):
    bottle_id = Bottle.query.get(id)
    bottle_id.delete_bottle()

    return redirect(url_for('main.collection',
                            name=current_user.username))


@main.route('/collection/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_bottle(id):
    bottle_id = Bottle.query.get(id)
    label = bottle_id.label

    edit_form = NewBottleForm(obj=bottle_id)

    if edit_form.validate_on_submit():

        if edit_form.photo.data:
            f = edit_form.photo.data
            fname = secure_filename(f.filename)
            f.save(os.path.join(create_app().config['UPLOADS_FOLDER'], fname))

            edit_form.populate_obj(bottle_id)
            bottle_id.photo = fname
            bottle_id.save_bottle()

        else:

            edit_form.populate_obj(bottle_id)
            bottle_id.save_bottle()

        return redirect(url_for('main.collection',
                                name=current_user.username))

    return render_template('new_bottle.html',
                           title='Edit {0}'.format(label),
                           bottle_form=edit_form,
                           originalbottle=bottle_id)


@main.route('/collection/<int:id>')
def single_bottle(id):
    onebottle = Bottle.query.get(id)

    if onebottle is None:
        abort(404)

    title = onebottle.label

    return render_template("bottle.html",
                           bottle=onebottle,
                           title=title)
