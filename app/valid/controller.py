from wtforms import Form, StringField, DecimalField
from wtforms.validators import length, NumberRange


class validate(Form):
    arg0 = DecimalField(label='参数1',validators=[NumberRange(min=1, max=5)])
    arg1 = StringField(label='参数2',validators=[length(min=1, max=5)], default='默认')
