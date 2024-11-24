
from .models import Category

def get_categories(reques):
    categories = Category.objects.all()
    return dict(categories=categories)