from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required

def index(request):
	context = {}
	return render(request, 'index.html', context)

def ml_algorithms(request):
    context = {}
    return render(request, 'ML_algorithms/0_ML_algorithms.html', context)

def num_methods(request):
	context = {}
	return render(request, 'Numerical_methods/0_Num_methods.html', context)

def supervised_learning(request):
    context = {}
    return render(request, 'ML_algorithms/1_Supervised_learning.html', context)

def lin_reg(request):
    context = {}
    return render(request, 'ML_algorithms/1_1_Linear_regression.html', context)

def root_finding(request):
	context = {}
	return render(request, 'Numerical_methods/1_1_Root_finding.html', context)
def bis_method(request):
	context = {}
	return render(request, 'Numerical_methods/1_1_1_Bisection_method.html', context)

def sort_alg(request):
	context = {}
	return render(request, 'Sorting_algorithms/0_Sorting_algorithms.html', context)

def bubble_sort(request):
	context = {}
	return render(request, 'Sorting_algorithms/bubble_sort.html', context)

def selection_sort(request):
	context = {}
	return render(request, 'Sorting_algorithms/selection_sort.html', context)