from django.shortcuts import render, redirect, get_object_or_404
from board.models import Advertisement
from board.forms import AdvertisementForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib import messages
from django.core.paginator import Paginator

def logout_view(request):
    '''
    Представление для выхода из систему пользователя
    :param request: запроос
    :return: Возвращает домашнюю страницу
    '''
    logout(request)
    return redirect('home')


from django.shortcuts import render, redirect
from .forms import SignUpForm
from django.contrib.auth import login, authenticate


def signup(request):
    '''
    Представление для регистрации в системе пользователя
    :param request: запрос
    :return: регистрирует пользователя в системе
    '''
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/board')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})


def home(request):
    '''
    Домашняя страница
    :param request: запрос
    :return: возвращает домашнюю страницу
    '''
    return render(request, 'home.html')


def advertisement_list(request):
    '''
    Представление для вывода всех объявлений
    :param request: запрос
    :return: Возвращает страницу с всеми объявлениями
    '''
    advertisements = Advertisement.objects.all()
    return render(request, 'board/advertisement_list.html', {'advertisements': advertisements})


def advertisement_detail(request, pk):
    '''
    Выводит конкретное объявление через id
    :param request: запрос
    :param pk: if
    :return: страницу с id объявлением
    '''
    advertisement = Advertisement.objects.get(pk=pk)
    return render(request, 'board/advertisement_detail.html', {'advertisement': advertisement})


@login_required
def edit_advertisement(request, pk):
    '''
    Представление для редактирования объявлений
    :param request: запрос
    :param pk: id объявления
    :return: Редактирует объявления и возращает страницу объявлений
    '''
    advertisement = Advertisement.objects.get(pk=pk)
    if request.method == "POST":
        form = AdvertisementForm(request.POST, request.FILES, instance=advertisement)
        if form.is_valid():
            advertisement.save()
            return redirect('board:advertisement_list')
    else:
        form = AdvertisementForm(instance=advertisement)
    return render(request, 'board/edit_advertisement.html', {'form': form, 'advertisement': advertisement})


@login_required
def add_advertisement(request):
    '''
    Представление для добавления объявления
    :param request: запрос
    :return: Добавляет объявление и выводит список представлений
    '''
    if request.method == "POST":
        form = AdvertisementForm(request.POST, request.FILES)
        if form.is_valid():
            advertisement = form.save(commit=False)
            advertisement.author = request.user
            advertisement.save()
            return redirect('board:advertisement_list')
    else:
        form = AdvertisementForm()
    return render(request, 'board/add_advertisement.html', {'form': form})


@login_required
def delete_advertisement(request, pk):
    '''
    Представление для удаления объявления
    :param request: запрос
    :param pk: id  объявления
    :return: Удаляет объявление и возвращает на страницу объявлений
    '''
    advertisement = Advertisement.objects.get(pk=pk)
    if request.method == "POST":
        advertisement.delete()
        messages.success(request, 'Объявление успешно удалено.')
        return redirect('board:advertisement_list')
    return render(request, 'board/delete_advertisement.html', {'advertisement': advertisement})


@login_required
def like_ad(request, pk):
    advertisement = Advertisement.objects.get(pk=pk)
    if request.method == "POST":
        advertisement.likes += 1
        advertisement.save()
        return redirect('board:advertisement_detail', pk=advertisement.pk)


@login_required
def dislike_ad(request, pk):
    advertisement = Advertisement.objects.get(pk=pk)
    if request.method == "POST":
        advertisement.dislikes += 1
        advertisement.save()
        return redirect('board:advertisement_detail', pk=advertisement.pk)

def advertisement_list(request):
    '''
    Представление для вывода всех объявлений с пагинацией
    :param request: запрос
    :return: Возвращает страницу с всеми объявлениями
    '''
    advertisements = Advertisement.objects.all()
    paginator = Paginator(advertisements, 3)  # Показывать 10 объявлений на странице

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'board/advertisement_list.html', {'page_obj': page_obj})