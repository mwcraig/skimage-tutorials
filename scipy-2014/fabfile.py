import fabric.api as fabric


NBCONVERT = 'ipython nbconvert {}'

BUILD_SLIDES =  NBCONVERT.format('--to slides {}')

NOTEBOOKS = ['0_color_and_exposure.ipynb',
             '1_image_filters.ipynb',
             '2_feature_detection.ipynb']


@fabric.task
def build_slides(exclude=None):
    """ Build slides of all default notebooks. """
    exclude = exclude or []
    filtered_notebooks = (nb for nb in NOTEBOOKS if nb not in exclude)
    for nb in filtered_notebooks:
        fabric.local(BUILD_SLIDES.format(nb))


@fabric.task
def slideshow(nb=0):
    """ Build slides of all default notebooks and start slide-show. """
    try:
        nb = NOTEBOOKS[int(nb)]
    except ValueError:
        pass
    build_slides(exclude=[nb])
    serve = BUILD_SLIDES.format('--post serve {}')
    fabric.local(serve.format(nb))
