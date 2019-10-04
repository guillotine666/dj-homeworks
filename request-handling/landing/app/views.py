from collections import Counter

from django.shortcuts import render_to_response


counter_show = Counter(original=0, alternative=0)
counter_click = Counter(original=0, alternative=0)


def index(request):
    from_landing = request.GET.get('from-landing')
    if from_landing == 'original':
        counter_click['original'] += 1
    elif from_landing == 'test':
        counter_click['alternative'] += 1
    return render_to_response('index.html')


def landing(request):
    ab_arg = request.GET.get('ab-test-arg')
    if ab_arg == 'original':
        counter_show['original'] += 1
        return render_to_response('landing.html')
    elif ab_arg == 'test':
        counter_show['alternative'] += 1
        return render_to_response('landing_alternate.html')
    else:
        return render_to_response('landing.html')


def stats(request):
    if not counter_show['alternative']:
        counter_show['alternative'] = 1
    if not counter_show['original']:
        counter_show['original'] = 1
    return render_to_response('stats.html', context={
        'test_conversion': format(counter_click['alternative'] / counter_show['alternative'], '.1f'),
        'original_conversion': format(counter_click['original'] / counter_show['original'], '.1f'),
    })
