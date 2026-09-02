from sqlalchemy import select
from sqlalchemy.orm import Session

from nextkalaapi.models.tag_model import Tag


# read
def get_tag(db: Session, tag_id: int) -> Tag | None:
    stmt = select(Tag).where(Tag.id == tag_id)
    return db.scalar(stmt)


def get_tags(db: Session) -> list[Tag]:
    stmt = select(Tag)
    return list(db.scalars(stmt).all())


# creat
def create_tag(db: Session, tag: Tag) -> Tag:
    db.add(tag)
    db.commit()
    db.refresh(tag)

    return tag


# update
def update_tag(db: Session, tag: Tag) -> Tag:
    db.refresh(tag)
    db.commit()
    return tag


# delete
def delete_tag(db: Session, tag_id: int) -> int | None:
    tag = select(Tag).where(Tag.id == tag_id)
    if tag is None:
        return None
    db.delete(tag)
    db.commit()
    return tag_id
