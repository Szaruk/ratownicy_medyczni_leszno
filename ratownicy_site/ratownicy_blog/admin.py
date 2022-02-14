from django.contrib import admin
from .models import Post, PostImage, StatisticsImage, AboutUs, MainInfo, InfoSection, InfoSectionDetails, InfoSectionTitle

class PostImageAdmin(admin.StackedInline):
    model = PostImage

class InfoSectionDetailsAdmin(admin.StackedInline):
    model = InfoSectionDetails

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    inlines = [PostImageAdmin]
    list_display = ('title', 'categories', 'slug', 'author', 'publish', 'status')
    list_filter = ('status', 'categories', 'created', 'publish', 'author')
    search_fields = ('title', 'text_post')
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ('author',)
    date_hierarchy = 'publish'
    ordering = ('status', 'publish')

    class Meta:
        model = Post

@admin.register(PostImage)
class PostImageAdmin(admin.ModelAdmin):
    list_display = ('images', 'post')
    ordering = ('post',)

@admin.register(StatisticsImage)
class StatisticsImageAdmin(admin.ModelAdmin):
    list_display = ('statisticsPublished', 'statisticsImage',)
    ordering = ('statisticsPublished',)

@admin.register(AboutUs)
class AboutUs(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(MainInfo)
class MainInfo(admin.ModelAdmin):
    list_display = ('MainText',)

@admin.register(InfoSectionTitle)
class InfoSectionTitle(admin.ModelAdmin):
    list_display = ('SectionTitle',)

@admin.register(InfoSection)
class InfoSection(admin.ModelAdmin):
    inlines = [InfoSectionDetailsAdmin]
    list_display = ('InfoSection',)

@admin.register(InfoSectionDetails)
class InfoSectionDetails(admin.ModelAdmin):
    list_display = ('InfoSectionText',)