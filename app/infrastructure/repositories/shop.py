from uuid import UUID
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from models.shop import Shop


class ShopRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_by_id(self, shop_id: UUID) -> Shop | None:
        stmt = select(Shop).where(Shop.id == shop_id)
        result = await self.session.execute(stmt)

        return result.scalar_one_or_none()

    async def get_by_name(self, shop_address: str) -> Shop | None:
        stmt = select(Shop).where(Shop.address == shop_address)
        result = await self.session.execute(stmt)

        return result.scalar_one_or_none()

    async def create(self, shop: Shop) -> Shop:
        self.session.add(shop)

        await self.session.flush()
        await self.session.refresh(shop)

        return shop

    async def update(self, shop: Shop) -> Shop:
        await self.session.flush()
        await self.session.refresh(shop)

        return shop

    async def delete(self, shop: Shop) -> None:
        await self.session.delete(shop)
        await self.session.flush()