from django.shortcuts import redirect, render
from django.views.generic import View
from django.contrib.postgres.search import SearchVector
from users.models import UserProfile
from .models import CompleteGig
from .forms import OverViewForm, PricingForm, DescriptionForm, MediaForm


class OverViewGigView(View):
    def get(self, request, *args, **kwargs):
        user_profile = UserProfile.objects.get(user=request.user)
        context = {
            'over_view_form': OverViewForm(),
            'user_profile': user_profile,
        }
        return render(request, 'gigs/over_view.html', context=context)

    def post(self, request, *args, **kwargs):
        user_profile = UserProfile.objects.get(user=request.user)
        form = OverViewForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.save()
            complete_gig = CompleteGig(user=user_profile, over_view=form)
            complete_gig.save()
            return redirect('gigs:pricing')
        context = {
            'over_view_form': form,
            'user_profile': user_profile,
        }
        return render(request, 'gigs/over_view.html', context=context)


class PricingGigView(View):
    def get(self, request, *args, **kwargs):
        user_profile = UserProfile.objects.get(user=request.user)
        context = {
            'pricing_form': PricingForm(),
            'user_profile': user_profile,
        }
        return render(request, 'gigs/pricing.html', context=context)

    def post(self, request, *args, **kwargs):
        user_profile = UserProfile.objects.get(user=request.user)
        form = PricingForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.save()
            complete_gig = CompleteGig.objects.get(
                user=user_profile, active=False)
            complete_gig.pricing = form
            complete_gig.save()
            return redirect('gigs:description')
        context = {
            'pricing_form': form,
            'user_profile': user_profile,
        }
        return render(request, 'gigs/pricing.html', context=context)


class DescriptionGigView(View):
    def get(self, request, *args, **kwargs):
        user_profile = UserProfile.objects.get(user=request.user)
        context = {
            'description_form': DescriptionForm(),
            'user_profile': user_profile,
        }
        return render(request, 'gigs/description.html', context=context)

    def post(self, request, *args, **kwargs):
        user_profile = UserProfile.objects.get(user=request.user)
        form = DescriptionForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.save()
            complete_gig = CompleteGig.objects.get(
                user=user_profile, active=False)
            complete_gig.description = form
            complete_gig.save()
            return redirect('gigs:media')

        context = {
            'description_form': form,
            'user_profile': user_profile,
        }
        return render(request, 'gigs/description.html', context=context)


class MediaGigView(View):
    def get(self, request, *args, **kwargs):
        user_profile = UserProfile.objects.get(user=request.user)
        context = {
            'media_form': MediaForm(),
            'user_profile': user_profile,
        }
        return render(request, 'gigs/media.html', context=context)

    def post(self, request, *args, **kwargs):
        user_profile = UserProfile.objects.get(user=request.user)
        form = MediaForm(request.POST, request.FILES)
        if form.is_valid():
            form = form.save(commit=False)
            form.save()
            complete_gig = CompleteGig.objects.get(
                user=user_profile, active=False)
            complete_gig.media = form
            complete_gig.active = True
            complete_gig.save()
            return redirect('partners:partner_gigs')

        context = {
            'media_form': form,
            'user_profile': user_profile,
        }
        return render(request, 'gigs/media.html', context=context)


class EditGigView(View):
    def get(self, request, gig_id, *args, **kwargs):
        user_profile = UserProfile.objects.get(user=request.user)
        gig = CompleteGig.objects.get(id=gig_id)
        context = {
            'over_view_form': OverViewForm(instance=gig.over_view),
            'pricing_form': PricingForm(instance=gig.pricing),
            'description_form': DescriptionForm(instance=gig.description),
            'media_form': MediaForm(),
            'user_profile': user_profile,
            'gig_id': gig.id
        }
        return render(request, 'gigs/edit-gig.html', context=context)

    def post(self, request, gig_id, *args, **kwargs):
        user_profile = UserProfile.objects.get(user=request.user)
        gig = CompleteGig.objects.get(id=gig_id)
        context = {
            'over_view_form': OverViewForm(instance=gig.over_view),
            'pricing_form': PricingForm(instance=gig.pricing),
            'description_form': DescriptionForm(instance=gig.description),
            'media_form': MediaForm(instance=gig.media),
            'user_profile': user_profile,
            'gig_id': gig.id,
            'active': ''
        }
        if 'title' in request.POST:
            up_dict = {"active": 'over-view'}
            context.update(up_dict)
            form = OverViewForm(request.POST, instance=gig.over_view)
            if form.is_valid():
                form = form.save(commit=False)
                form.save()
                gig = CompleteGig.objects.get(id=gig_id)
                up_dict = {"over_view_form": OverViewForm(
                    instance=gig.over_view)}
                context.update(up_dict)
                return render(request, 'gigs/edit-gig.html', context=context)
            up_dict = {"over_view_form": form}
            context.update(up_dict)
        if 'name' in request.POST:
            up_dict = {"active": 'pricing'}
            context.update(up_dict)
            form = PricingForm(request.POST, instance=gig.pricing)
            if form.is_valid():
                form = form.save(commit=False)
                form.save()
                gig = CompleteGig.objects.get(id=gig_id)
                up_dict = {"pricing_form": PricingForm(
                    instance=gig.pricing)}
                context.update(up_dict)
                return render(request, 'gigs/edit-gig.html', context=context)
            up_dict = {"pricing": form}
            context.update(up_dict)
        if 'description' in request.POST:
            up_dict = {"active": 'description'}
            context.update(up_dict)
            form = DescriptionForm(request.POST, instance=gig.description)
            if form.is_valid():
                form = form.save(commit=False)
                form.save()
                gig = CompleteGig.objects.get(id=gig_id)
                up_dict = {"description_form": DescriptionForm(
                    instance=gig.description)}
                context.update(up_dict)
                return render(request, 'gigs/edit-gig.html', context=context)
            up_dict = {"description_form": form}
            context.update(up_dict)
        if 'main_image' in request.POST or request.FILES:
            up_dict = {"active": 'media'}
            context.update(up_dict)
            form = MediaForm(request.POST, request.FILES, instance=gig.media
                             )
            if form.is_valid():
                form = form.save(commit=False)
                form.save()
                gig = CompleteGig.objects.get(id=gig_id)
                gig.media = form
                gig.save()
                up_dict = {"media_form": MediaForm(
                    instance=gig.media)}
                context.update(up_dict)
                return render(request, 'gigs/edit-gig.html', context=context)
            up_dict = {"media_form": form}
            context.update(up_dict)
        return render(request, 'gigs/edit-gig.html', context=context)


class DeleteGigView(View):
    def get(self, request, gig_id, *args, **kwargs):
        CompleteGig.objects.get(id=gig_id).delete()
        return redirect('partners:partner_gigs')


class ContinueGigView(View):
    def get(self, request, gig_id, *args, **kwargs):
        gig = CompleteGig.objects.get(id=gig_id)
        if not gig.pricing:
            return redirect('gigs:pricing')
        if not gig.description:
            return redirect('gigs:description')
        if not gig.media:
            return redirect('gigs:media')


class GigsView(View):
    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            user_profile = None
        else:
            user_profile = UserProfile.objects.get(user=request.user)
        context = {
            'user_profile': user_profile,
            'gigs': '',
            'home': True,
            'tags': '',
            'target': request.POST['search']
        }
        if request.method == 'POST':
            gigs = CompleteGig.objects.annotate(
                search=SearchVector('over_view__title') +
                SearchVector('over_view__search_tags') + SearchVector(
                    'over_view__sub_category__name') + SearchVector('over_view__sub_category__category__name'),
            ).filter(search=request.POST['search'])
            if 'budget' in request.POST:
                budget = request.POST['budget'].split(',')
                gigs = gigs.filter(pricing__price__gte=budget[0],
                                   pricing__price__lte=budget[1]
                                   )
            if gigs:
                tags = []
                for i in gigs:
                    tags_list = i.over_view.search_tags.split(',')
                    for tag in tags_list:
                        if not tag in tags:
                            tags.append(tag)
                up_dict = {'tags': tags}
                context.update(up_dict)
            up_dict = {'gigs': gigs, 'home': False}
            context.update(up_dict)
            return render(request, 'gigs/gigs.html', context=context)
        return render(request, 'pages/home.html', context=context)


class GigDetailView(View):
    def get(self, request, gig_id,  *args, **kwargs):
        user_profile = UserProfile.objects.get(user=request.user)
        gig = CompleteGig.objects.get(id=gig_id)
        tags_list = gig.over_view.search_tags
        tags_list = tags_list.split(',')
        context = {
            'user_profile': user_profile,
            'gig': gig,
            'tags_list': tags_list
        }
        return render(request, 'gigs/gig-detail.html', context=context)

    def post(self, request, *args, **kwargs):
        user_profile = UserProfile.objects.get(user=request.user)
        form = DescriptionForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.save()
            complete_gig = CompleteGig.objects.get(
                user=user_profile, active=False)
            complete_gig.description = form
            complete_gig.save()
            return redirect('gigs:media')

        context = {
            'description_form': form,
            'user_profile': user_profile,
        }
        return render(request, 'gigs/description.html', context=context)
