from django.db.models.query import sync_to_async
from main.models import CV
from .base import BaseRepository


class CvRepository(BaseRepository):
    async def fetch_cv_by_id(self, id: int) -> CV:
        cv = await sync_to_async(
            lambda : CV.objects.get(id=id)
        )()
        return cv
