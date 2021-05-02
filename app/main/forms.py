from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, SelectField, TextAreaField, SubmitField
from wtforms.validators import InputRequired

region_choices = ['Aichi', 'Akita', 'Aomori', 'Chiba', 'Ehime', 'Fukui', 'Fukuoka', 'Fukushima', 'Gifu', 'Gunma',
                  'Hyogo', 'Hokkaido', 'Hiroshima', 'Iwate', 'Ibaraki', 'Ishikawa', 'Kochi', 'Kyoto', 'Kagawa',
                  'Kumamoto', 'Kanagawa', 'Kagoshima', 'Mie', 'Miyagi', 'Miyazaki', 'Nara', 'Nagano', 'Niigata',
                  'Nagasaki', 'Oita', 'Osaka', 'Okayama', 'Okinawa', 'Saga', 'Shiga', 'Shimane', 'Saitama', 'Shizuoka',
                  'Tokyo', 'Toyama', 'Tottori', 'Tochigi', 'Tokushima', 'Wakayama', 'Yamagata', 'Yamaguchi',
                  'Yamanashi', "Don't know or don't care"]


class NewBottleForm(FlaskForm):
    label = StringField('Label', validators=[InputRequired()])
    identifier = TextAreaField('Identifier')
    photo = FileField('Photo', validators=[FileAllowed(['png', 'jpeg', 'jpg', 'gif'], 'Incorrect file format')])
    category = SelectField('Category', choices=["Honjozo-shu", "Junmai-shu", "Ginjo-shu", "Junmai Ginjo-shu",
                                                "Daiginjo-shu", "Junmai Daiginjo-shu"], validators=[InputRequired()])
    maker = StringField('Maker', validators=[InputRequired()])
    status = SelectField('Status', choices=['Unopened', 'Opened', 'Finished'], validators=[InputRequired()])
    region = SelectField('Region', choices=region_choices, validators=[InputRequired()])
    price = StringField(validators=[InputRequired()])
    notes = TextAreaField('Notes')
    submit = SubmitField('Submit')
