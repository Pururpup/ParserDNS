from uuid import UUID
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from models.brand import Brand


class BrandRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_by_id(self, brand_id: UUID) -> Brand | None:
        stmt = select(Brand).where(Brand.id == brand_id)
        result = await self.session.execute(stmt)

        return result.scalar_one_or_none()

    async def get_by_name(self, brand_name: str) -> Brand | None:
        stmt = select(Brand).where(Brand.brand_name == brand_name)
        result = await self.session.execute(stmt)

        return result.scalar_one_or_none()

    async def create(self, brand: Brand) -> Brand:
        self.session.add(brand)

        await self.session.flush()
        await self.session.refresh(brand)

        return brand

    async def update(self, brand: Brand) -> Brand:
        await self.session.flush()
        await self.session.refresh(brand)

        return brand

    async def delete(self, brand: Brand) -> None:
        await self.session.delete(brand)
        await self.session.flush()