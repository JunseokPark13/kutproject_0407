from django.http import HttpResponse

def hello(request, to):                 # 핸들러 선언. 언제나 첫번째 인자는 request 객체입니다. request 파라미터 이후에 url패턴을 통해 전달받을 파라미터들을 선언합니다.
                                        # 이 때 파라미터이름은 url패턴에서 사용된 변수의 이름과 동일해야 합니다.(키워드인자이기 때문에)
    return HttpResponse('Hello {}.'.format(to))
