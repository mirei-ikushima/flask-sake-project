from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, SelectField, TextAreaField, DecimalField, SubmitField
from wtforms.validators import InputRequired, Optional

region_choices = ['Hokkaido', 'Aomori', 'Iwate', 'Miyagi', 'Akita', 'Yamagata', 'Fukushima', 'Ibaraki', 'Tochigi',
                  'Gunma', 'Saitama', 'Chiba', 'Tokyo', 'Kanagawa', 'Niigata', 'Toyama', 'Ishikawa', 'Fukui',
                  'Yamanashi', 'Nagano', 'Gifu', 'Shizuoka', 'Aichi', 'Mie', 'Shiga', 'Kyoto', 'Osaka', 'Hyogo', 'Nara',
                  'Wakayama', 'Tottori', 'Shimane', 'Okayama', 'Hiroshima', 'Yamaguchi', 'Tokushima', 'Kagawa', 'Ehime',
                  'Kochi', 'Fukuoka', 'Saga', 'Nagasaki', 'Kumamoto', 'Oita', 'Miyazaki', 'Kagoshima', 'Okinawa']


class NewBottleForm(FlaskForm):
    label = StringField('Label', validators=[InputRequired()])
    identifier = TextAreaField("Identifier")
    photo = FileField('Photo', validators=[FileAllowed(['png', 'jpeg', 'jpg', 'gif'], 'Incorrect file format')])
    category = SelectField('Category', choices=["Honjozo-shu", "Junmai-shu", "Ginjo-shu", "Junmai Ginjo-shu",
                                                "Daiginjo-shu", "Junmai Daiginjo-shu"], validators=[InputRequired()])
    maker = StringField('Maker', validators=[InputRequired()])
    status = SelectField('Status', choices=['Unopened', 'Opened', 'Finished'], validators=[InputRequired()])
    region = SelectField('Region', choices=region_choices, validators=[InputRequired()])
    price = DecimalField(validators=[InputRequired()])
    submit = SubmitField('Submit')
