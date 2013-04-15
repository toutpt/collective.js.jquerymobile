from setuptools import setup, find_packages

version = '1.3.1.0'

setup(name='collective.js.jquerymobile',
      version=version,
      description="JQuery mobile integration in Plone",
      long_description=open("README.rst").read() + "\n" +
                       open("CHANGES.txt").read(),
      # Get more strings from
      # http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Environment :: Web Environment",
        "License :: OSI Approved :: GNU General Public License (GPL)",
        "Operating System :: OS Independent",
        "Framework :: Zope2",
        "Framework :: Plone",
        "Framework :: Plone :: 4.0",
        "Framework :: Plone :: 4.1",
        "Framework :: Plone :: 4.2",
        "Framework :: Plone :: 4.3",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
      ],
      keywords='plone jquery mobile',
      author='JeanMichel FRANCOIS aka toutpt',
      author_email='toutpt@gmail.com',
      url='https://github.com/toutpt/collective.js.jquerymobile',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['collective', 'collective.js'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'plone.app.jquery',
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
