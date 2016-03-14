import unittest

#from zope.testing import doctestunit
#from zope.component import testing
from Testing import ZopeTestCase as ztc

from Products.Five import fiveconfigure
from Products.PloneTestCase import PloneTestCase as ptc
from Products.PloneTestCase.layer import PloneSite
ptc.setupPloneSite()

import collective.favicon

PACKAGE_NAME = "collective.favicon"

class TestCase(ptc.PloneTestCase):

    class layer(PloneSite):

        @classmethod
        def setUp(cls):
            fiveconfigure.debug_mode = True
            ztc.installPackage(collective.favicon)
            fiveconfigure.debug_mode = False

        @classmethod
        def tearDown(cls):
            pass

class TestInstall(TestCase):

    def test_install(self):
        qi = self.portal.portal_quickinstaller
        self.failUnless(PACKAGE_NAME in (p['id'] for p in qi.listInstallableProducts()))
        qi.installProduct(PACKAGE_NAME)
        self.failUnless(qi.isProductInstalled(PACKAGE_NAME))

class TestControlpanel(TestCase):

    def afterSetUp(self):
        self.setRoles(('Manager',))
        qi = self.portal.portal_quickinstaller
        qi.installProduct(PACKAGE_NAME)

    def test_has_panel(self):
        pass
        "collective-favicon-settings"

    def test_has_recode(self):
        pass

    def test_file_widget(self):
        pass


def test_suite():
    return unittest.TestSuite([

        unittest.makeSuite(TestInstall),
        unittest.makeSuite(TestControlpanel),

        # Unit tests
        #doctestunit.DocFileSuite(
        #    'README.txt', package='collective.favicon',
        #    setUp=testing.setUp, tearDown=testing.tearDown),

        #doctestunit.DocTestSuite(
        #    module='collective.favicon.mymodule',
        #    setUp=testing.setUp, tearDown=testing.tearDown),


        # Integration tests that use PloneTestCase
        # ztc.ZopeDocFileSuite(
        #    'README.txt', package='collective.favicon',
        #    test_class=TestCase),

        #ztc.FunctionalDocFileSuite(
        #    'browser.txt', package='collective.favicon',
        #    test_class=TestCase),

        ])

if __name__ == '__main__':
    unittest.main(defaultTest='test_suite')
