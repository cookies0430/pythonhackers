from sqlalchemy.dialects import postgresql
from pyhackers.db import DB as db
from pyhackers.common import format_date


class Tutorial(db.Model):
    __tablename__ = "tutorial"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    user_id = db.Column(db.BigInteger, db.ForeignKey('user.id'), index=True)
    user = db.relationship("User", )

    title = db.Column(db.Text, nullable=False)
    slug = db.Column(db.Text, nullable=False, index=True)

    keywords = db.Column(db.Text, nullable=False)
    meta_description = db.Column(db.Text, nullable=False)

    content = db.Column(db.Text, nullable=False)
    content_html = db.Column(db.Text, nullable=False)

    created_at = db.Column(db.DateTime)
    generated_at = db.Column(db.DateTime)

    publish = db.Column(db.Boolean, default=True)
    spam = db.Column(db.Boolean, default=False)

    upvote_count = db.Column(db.Integer, default=1)

    @staticmethod
    def to_dict(obj):
        assert isinstance(obj, Tutorial)

        return {
            'id': unicode(obj.id),
            'title': unicode(obj.name),
            'slug': unicode(obj.slug),
            'created_at': unicode(format_date(obj.created_at)),
            'generated_at': unicode(format_date(obj.generated_at)),
            'keywords': unicode(obj.keywords),
            'content': unicode(obj.content),
            'content_html': unicode(obj.content_html),
            'meta_description': unicode(obj.meta_description),
            'upvote_count': obj.upvote_count or 0,
            'spam': obj.spam
        }

    def __repr__(self):
        return str(Tutorial.to_dict(self))

    def __str__(self):
        return str(self.name)