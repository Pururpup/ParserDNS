from uuid import UUID
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from models.item import Item


class ItemRepository:
    def __init__(self, session: AsyncSession):
        self.session = session # подключаем к бд

    async def get_by_id(self, item_id: UUID) -> Item | None:
        stmt = select(Item).where(Item.id == item_id)
        result = await self.session.execute(stmt)

        return result.scalar_one_or_none()

    async def get_by_external_id(self, external_id: str) -> Item | None:
        stmt = select(Item).where(Item.external_id == external_id)
        result = await self.session.execute(stmt)

        return result.scalar_one_or_none()

    async def create(self, item: Item) -> Item:
        self.session.add(item)

        await self.session.flush() # отправляет INSERT в бд
        await self.session.refresh(item) # подгружает обновленные поля

        return item

    async def update(self, item: Item) -> Item:
        await self.session.flush()
        await self.session.refresh(item)

        return item

    async def delete(self, item: Item) -> None:
        await self.session.delete(item)
        await self.session.flush()