import collections
import urllib.parse

from appdata.models import CountryModel, StateCasesModel


def slug_for_country():
    country_objs = CountryModel.objects.all().order_by('id')
    count = 0
    for country_obj in country_objs:
        try:
            print(count)
            country_name = country_obj.name.replace('-', ' ')
            split_country_name = country_name.split()
            demo_list = []
            for each_value in split_country_name:
                slug_without_commas = each_value.replace(',', '')
                slug_without_fullstops = slug_without_commas.replace('.', '')
                slug_without_slash = slug_without_fullstops.replace('/', '-')
                slug_without_percent_sign = slug_without_slash.replace('%', '')
                slug_without_left_open_brackets = slug_without_percent_sign.replace('(', '')
                slug_without_left_close_brackets = slug_without_left_open_brackets.replace('[', '')
                slug_without_right_open_brackets = slug_without_left_close_brackets.replace(')', '')
                slug_without_right_close_brackets = slug_without_right_open_brackets.replace(']', '').lower()
                new_slug = slug_without_right_close_brackets.replace(' ', '-')
                # print("this is slug: ", new_slug)
                if new_slug.strip() == '':
                    print("if statement", new_slug)
                else:
                    demo_list.append(new_slug)
                    dev_slug = '-'.join(demo_list)
            unique_slug = dev_slug
            num = 1
            while CountryModel.objects.filter(slug=unique_slug).exists():
                unique_slug = '{}-{}'.format(dev_slug, num)
                num += 1
            print(unique_slug)
            country_obj.slug = unique_slug
            count += 1
            country_obj.save()
        except Exception as e:
            print(e)
            f = open('business_slug_error.txt', 'a')
            f.write(("Id : "+str(country_obj.id) + " city name : "+str(country_obj.name) + " error: "+str(e)) + "\n")
            f.close()

# from slug_modifier import slug_for_country


def slug_for_state():
    state_objs = StateCasesModel.objects.all().order_by('id')
    count = 0
    for state_obj in state_objs:
        try:
            print(count)
            state_name = state_obj.name.replace('-', ' ')
            split_state_name = state_name.split()
            demo_list = []
            for each_value in split_state_name:
                slug_without_commas = each_value.replace(',', '')
                slug_without_fullstops = slug_without_commas.replace('.', '')
                slug_without_slash = slug_without_fullstops.replace('/', '-')
                slug_without_percent_sign = slug_without_slash.replace('%', '')
                slug_without_left_open_brackets = slug_without_percent_sign.replace('(', '')
                slug_without_left_close_brackets = slug_without_left_open_brackets.replace('[', '')
                slug_without_right_open_brackets = slug_without_left_close_brackets.replace(')', '')
                slug_without_right_close_brackets = slug_without_right_open_brackets.replace(']', '').lower()
                new_slug = slug_without_right_close_brackets.replace(' ', '-')
                # print("this is slug: ", new_slug)
                if new_slug.strip() == '':
                    print("if statement", new_slug)
                else:
                    demo_list.append(new_slug)
                    dev_slug = '-'.join(demo_list)
            unique_slug = dev_slug
            num = 1
            while StateCasesModel.objects.filter(slug=unique_slug).exists():
                unique_slug = '{}-{}'.format(dev_slug, num)
                num += 1
            print(unique_slug)
            state_obj.slug = unique_slug
            count += 1
            state_obj.save()
        except Exception as e:
            print(e)
            f = open('business_slug_error.txt', 'a')
            f.write(("Id : "+str(state_obj.id) + " city name : "+str(state_obj.name) + " error: "+str(e)) + "\n")
            f.close()

# from slug_modifier import slug_for_state