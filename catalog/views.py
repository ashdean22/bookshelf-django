from django.shortcuts import render, get_object_or_404, redirect
from .models import Book
from .forms import BookForm
from django.contrib.auth.decorators import login_required
from rest_framework import generics
from .serializers import BookSerializer
from rest_framework import generics, permissions


def book_list(request):
    query = request.GET.get("q", "")
    books = Book.objects.select_related("author").prefetch_related("categories")
    if query:
        books = books.filter(title__icontains=query)
    return render(request, "catalog/book_list.html", {
        "books": books,
        "query": query,
    })


def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, "catalog/book_detail.html", {"book": book})

@login_required
def book_create(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            book = form.save()
            return redirect("catalog:book_detail", pk=book.pk)
    else:
        form = BookForm()

    return render(request, "catalog/book_form.html", {"form": form})


from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

class BookCreateView(CreateView):
    model = Book
    form_class = BookForm
    template_name = "catalog/book_form.html"

    def get_success_url(self):
        return reverse_lazy("catalog:book_detail", kwargs={"pk": self.object.pk})


class BookListAPIView(generics.ListCreateAPIView):
    queryset = Book.objects.select_related("author").prefetch_related("categories")
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class BookDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.select_related("author").prefetch_related("categories")
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]