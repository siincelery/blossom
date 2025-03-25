from django.db.models import Q
from goods.models import Products
from django.contrib.postgres.search import (
    SearchVector,
    SearchQuery,
    SearchRank,
    SearchHeadline,
)

def q_search(query):
    if query.isdigit() and len(query) <= 5:
        return Products.objects.filter(id=int(query))
    
    # Включаем все нужные поля в поисковый вектор
    vector = SearchVector("name", "description", "pyramid_of_fragrance", "type_product", "type_of_personality__name")
    query = SearchQuery(query)

    result = (
        Products.objects.annotate(rank=SearchRank(vector, query))
        .filter(rank__gt=0)
        .order_by("-rank")
    )

    # Добавляем подсветку только для тех полей, которые хотим показывать
    result = result.annotate(
        headline=SearchHeadline(
            "name",
            query,
            start_sel='<span style="background-color: #D3D3D3;">',
            stop_sel="</span>",
        )
    )
    result = result.annotate(
        bodyline=SearchHeadline(
            "description",
            query,
            start_sel='<span style="background-color: #D3D3D3;">',
            stop_sel="</span>",
        )
    )
    
    return result