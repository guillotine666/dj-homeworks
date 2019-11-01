from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet
from .models import Article, Scope, ArticleScope


class AboutScopeInlineFormset(BaseInlineFormSet):
    def clean(self):
        selected_topics = 0
        for form in self.forms:
            if form.cleaned_data and form.cleaned_data['is_main']:
                selected_topics += 1
        if selected_topics == 0:
            raise ValidationError('Нет основного раздела')
        if selected_topics > 1:
            raise ValidationError('Должен быть один основной раздел')

        return super().clean()


class ArticlesScopeInline(admin.TabularInline):
    model = ArticleScope
    formset = AboutScopeInlineFormset
    extra = 1


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = (ArticlesScopeInline,)


@admin.register(Scope)
class ScopeAdmin(admin.ModelAdmin):
    # inlines = (ArticlesScopeInline,)
    pass
