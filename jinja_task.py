from jinja2 import Template

# 1
name = 'Иван'

tm = Template('Привет {{ name }}')
msg = tm.render(name=name)

print(msg)

# 2
cities = [{'id': 1, 'city': 'Москва'},
          {'id': 2, 'city': 'Тверь'},
          {'id': 7, 'city': 'Минск'},
          {'id': 8, 'city': 'Саратов'}]

link = '''<select name="cities">
{% for c in cities -%}
{% if c.id > 6 -%}
    <option value="{{c['id']}}">{{c['city']}}</option>
{%elif c.city == "Москва" -%}
    <option>{{c['city']}}</option>
{%else -%}
    {{c['city']}}
{% endif -%}
{% endfor -%}
</select>'''

tm = Template(link)
msg = tm.render(cities=cities)

print(msg)

# 3
cars = [
    {'model': 'Ауди', 'price': 23000},
    {'model': 'Шкода', 'price': 27000},
    {'model': 'Вольво', 'price': 30000}]

tpl = "Суммарная цена {{ cs | sum(attribute='price') }}"
tm = Template(tpl)
msg = tm.render(cs=cars)

print(msg)

# 4
tpl = "Максимальная цена {{ cs | max(attribute='price') }}"
tm = Template(tpl)
msg = tm.render(cs=cars)

print(msg)

# 5
persons = [
    {'name': 'Алексей', 'age': 23},
    {'name': 'Александр', 'age': 27},
    {'name': 'Владимир', 'age': 30}]

tpl = '''
{%- for u in users -%}
{% filter upper %}{{u.name}}{% endfilter %}
{% endfor %}
'''
tm = Template(tpl)
msg = tm.render(users=persons)

print(msg)

# 6
html = '''
{% macro input(name, value ='', type='text', size=20) -%}
    <input type="{{ type }}" name="{{ name }}" value="{{ value }}"\
size="{{ size }}">
{%- endmacro %}

<p>{{ input('username') }}
<p>{{ input('email') }}
<p>{{ input('password') }}
'''
tm = Template(html)
msg = tm.render()

print(msg)

# 7
persons = [
    {'name': 'Алексей', 'age': 23, 'weight': 78},
    {'name': 'Александр', 'age': 27, 'weight': 82},
    {'name': 'Владимир', 'age': 30, 'weight': 77}]

html = '''
{% macro list_users(list_of_users) -%}
<ul>
{%- for u in list_of_users -%}
    <li>{{u.name}} {{caller(u)}}
{% endfor %}
</ul>
{%- endmacro %}

{% call(user) list_users(users) %}
    <ul>
    <li>age: {{user.ege}}
    <li>weight: {{user.weight}}
    </ul>
{% endcall -%}
'''

tm = Template(html)
msg = tm.render(users=persons)

print(msg)
