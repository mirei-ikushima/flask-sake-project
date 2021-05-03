from flask_wtf import FlaskForm
from flask_babel import lazy_gettext as _l
from flask_babel import _
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, SelectField, TextAreaField, SubmitField
from wtforms.validators import InputRequired

region_choices = [_l('Aichi'), _l('Akita'), _l('Aomori'), _l('Chiba'), _l('Ehime'), _l('Fukui'), _l('Fukuoka'),
                  _l('Fukushima'), _l('Gifu'), _l('Gunma'), _l('Hyogo'), _l('Hokkaido'), _l('Hiroshima'), _l('Iwate'),
                  _l('Ibaraki'), _l('Ishikawa'), _l('Kochi'), _l('Kyoto'), _l('Kagawa'), _l('Kumamoto'), _l('Kanagawa'),
                  _l('Kagoshima'), _l('Mie'), _l('Miyagi'), _l('Miyazaki'), _l('Nara'), _l('Nagano'), _l('Niigata'),
                  _l('Nagasaki'), _l('Oita'), _l('Osaka'), _l('Okayama'), _l('Okinawa'), _l('Saga'), _l('Shiga'),
                  _l('Shimane'), _l('Saitama'), _l('Shizuoka'), _l('Tokyo'), _l('Toyama'), _l('Tottori'), _l('Tochigi'),
                  _l('Tokushima'), _l('Wakayama'), _l('Yamagata'), _l('Yamaguchi'), _l('Yamanashi'),
                  _l("Don't know or don't care")]


class NewBottleForm(FlaskForm):
    label = StringField(_l('Label'), validators=[InputRequired()])
    identifier = TextAreaField(_l('Identifier'))
    photo = FileField(_l('Photo'), validators=[FileAllowed(['png', 'jpeg', 'jpg', 'gif'], _('Incorrect file format'))])
    category = SelectField(_l('Category'), choices=[_l("Honjozo-shu"), _l("Junmai-shu"), _l("Ginjo-shu"),
                                                    _l("Junmai Ginjo-shu"), _l("Daiginjo-shu"),
                                                    _l("Junmai Daiginjo-shu")], validators=[InputRequired()])
    maker = StringField(_l('Maker'), validators=[InputRequired()])
    status = SelectField(_l('Status'), choices=[_l('Unopened'), _l('Opened'), _l('Finished')],
                         validators=[InputRequired()])
    region = SelectField(_l('Region'), choices=region_choices, validators=[InputRequired()])
    price = StringField(_l('Price'), validators=[InputRequired()])
    notes = TextAreaField(_l('Notes'))
    submit = SubmitField(_l('Submit'))
