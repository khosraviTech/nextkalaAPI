from sqlalchemy import true, update
from sqlalchemy.orm import Session

from nextkalaapi.models.tag_model import Tag
from nextkalaapi.repositories import tag_repository
from nextkalaapi.schemas.tag import TagInsert, TagUpdate


# read
def get_tag(db: Session, tag_id: int) -> Tag | None:
    return tag_repository.get_tag(db, tag_id)


def get_tags(db: Session) -> list[Tag]:
    return tag_repository.get_tags(db)


# create
def create_tag(db: Session, tag_data: TagInsert) -> Tag:
    return tag_repository.create_tag(db, **tag_data.model_dump())


# update
def update_tag(db: Session, tag_id: int, tag_data: TagUpdate) -> Tag | None:
    tag = tag_repository.get_tag(db, tag_id)
    if tag is None:
        return None
    update_data = tag_data.model_dump(exclude_unset=true)
    for field, value in update_data.items():
        if field != "id":
            setattr(tag, field, value)
    return tag


# delete
def delete_tag(db: Session, tag_id: int) -> int | None:
    return tag_repository.delete_tag(tag_id)
