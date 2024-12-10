from django.core.management.base import BaseCommand
from shop.models import Category, Item, Tag
from django.db.models import Sum, Avg, Count, Min, Max
from django.contrib.contenttypes.models import ContentType

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        categories_with_counts = Category.categories.with_item_count()
        for category in categories_with_counts:
            print(f"Category: {category.name}, Item count: {category.item_count}")

        items_with_counts = Item.items.with_tag_count()
        for item in items_with_counts:
            print(f"Item: {item.name}, Tag count: {item.tag_count}")

        popular_tags = Tag.tags.popular_tags(9)
        for tag in popular_tags:
            print(f"Tag: {tag.name}, Item count: {tag.item_count}")