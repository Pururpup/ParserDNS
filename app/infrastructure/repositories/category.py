from uuid import UUID
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from models.category import Category


class CategoryRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_by_id(self, category_id: UUID) -> Category | None:
        stmt = select(Category).where(Category.id == category_id)
        result = await self.session.execute(stmt)

        return result.scalar_one_or_none()

    async def get_by_name(self, category_name: str) -> Category | None:
        stmt = select(Category).where(Category.category_name == category_name)
        result = await self.session.execute(stmt)

        return result.scalar_one_or_none()

    async def create(self, category: Category) -> Category:
        self.session.add(category)

        await self.session.flush()
        await self.session.refresh(category)

        return category

    async def update(self, category: Category) -> Category:
        await self.session.flush()
        await self.session.refresh(category)

        return category

    async def delete(self, category: Category) -> None:
        await self.session.delete(category)
        await self.session.flush()