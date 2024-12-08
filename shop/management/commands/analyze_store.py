from django.core.management.base import BaseCommand
from shop.models import Category, Item, Tag
from django.db.models import (
    Sum,
    Avg,
    Count,
    Min,
    Max
)

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        item_count = Category.objects.aggregate(all_items=Count('items'))
        print(item_count)

        item_max_min_avg = Category.objects.aggregate(max_price=Max('items__price'), min_price=Min('items__price'), avg_price=Avg('items__price'))
        print(item_max_min_avg)

        category_items = Category.objects.annotate(count=Count('items'))
        for category in category_items:
            print(f'{category.name}: {category.count}')

        category_sum = Category.objects.annotate(summed=Sum('items__price', default = 0))
        for category in category_sum:
            print(f'{category.name}: {category.summed}')

        item_catgs = Item.objects.select_related('category').all()
        for items in item_catgs:
            print(f'{items.name}: {items.category.name}')

        all_tags = Tag.objects.prefetch_related('items').all()
        for tags in all_tags:
            print(f'{tags.name}: {[item.name for item in tags.items.all()]}')



