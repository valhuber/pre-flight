# coding: utf-8
from safrs import SAFRSBase
from flask_sqlalchemy.model import Model

class AlsBase(SAFRSBase):
    """ SQLAlchemy super mixin, extending SAFRSBase 

    Eliminate startup 'pre-flight' SQLs
    * override the _s_sample() and _s_sample_dict()

    You typically do not modify this class,
    but you can to alter SAFRS behavior.
    """

    pre_flight = False
    """ True means execute pre-flight sqls on each class """

    def __init__(self, *args, **kwargs):
        super.__init__(*args, **kwargs)

    @classmethod
    def _s_sample_id(cls):
        if cls.pre_flight:
            super._s_sample_id(cls)
        else:
            return None

    @classmethod
    def _s_sample_dict(cls):
        if cls.pre_flight:
            super._s_sample_dict(cls)
        else:
            return {}
