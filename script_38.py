
text_styles = [
    ('awesome', '^'),
    ('text', '-'),
    ('formatting', '*'),
    ('using', '%'),
    ('format()', '!')
]

for text, deco in text_styles:
    design_fmt = '{:%s^20}' % deco
    print(design_fmt.format(text))

"""
^^^^^^awesome^^^^^^^
--------text--------
*****formatting*****
%%%%%%%using%%%%%%%%
!!!!!!format()!!!!!!
"""
