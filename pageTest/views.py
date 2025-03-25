from django.shortcuts import render, redirect
from pageTest.models import Question, TypesOfPersonality
from goods.models import Products

def personality_test(request):
    # Если есть сохранённые результаты - показываем их
    if 'personality_type' in request.session:
        return redirect('personality_test:result')
    
    questions = Question.objects.all()

    if request.method == 'POST':
        scores = {
            'Интроверт': 0,
            'Амбиверт': 0,
            'Экстраверт': 0,
        }

        for question in questions:
            answer = request.POST.get(f'question_{question.id}')
            if answer == 'yes':
                scores[question.type_of_personality.name] += question.weight
            elif answer == 'no':
                scores[question.type_of_personality.name] -= question.weight

        personality_type_name = max(scores, key=scores.get)
        personality_type = TypesOfPersonality.objects.get(name=personality_type_name)
        perfumes = Products.objects.filter(type_of_personality=personality_type)

        request.session['personality_type'] = {
            'name': personality_type.name,
            'description': personality_type.description,
        }
        request.session['perfumes'] = [
            {
                'name': product.name,
                'slug': product.slug,
                'description': product.description,
                'image': product.image.url if product.image else None,
                'price': str(product.price),
                'discount': str(product.discount),
                'sell_price': str(product.sell_price()),
                'display_id': product.display_id(),
            }
            for product in perfumes
        ]

        return redirect('personality_test:result')

    return render(request, 'pageTest/pageTest.html', {'questions': questions})

def result_page_test(request):
    personality_type = request.session.get('personality_type')
    perfumes = request.session.get('perfumes')
    
    if not personality_type or not perfumes:
        return redirect('personality_test:pageTest')
    
    return render(request, 'pageTest/resultPageTest.html', {
        'personality_type': personality_type,
        'perfumes': perfumes,
    })

def reset_test(request):
    if 'personality_type' in request.session:
        del request.session['personality_type']
    if 'perfumes' in request.session:
        del request.session['perfumes']
    return redirect('personality_test:pageTest')