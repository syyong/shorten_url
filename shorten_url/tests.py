from django.test import TestCase

from shorten_url.models import Redirect
import id_encoder

# pylint: disable=no-member,no-self-use
class RedirectModelTest(TestCase):

    def setUp(self):
        self.urls = [
            "https://docs.djangoproject.com/en/2.2/intro/tutorial05/",
            "https://docs.djangoproject.com/en/2.2/ref/models/fields/#field-types",
        ]

    def create_redirect(self, url):
        redirect = Redirect()
        redirect.destination = url
        redirect.save()
        return redirect

    def test_saving_and_retrieving_redirects(self):

        redirects = [self.create_redirect(u) for u in self.urls]

        self.assertEqual(
            Redirect.objects.all().count(),
            len(redirects)
        )

        for i, redirect in enumerate(redirects):
            self.assertEqual(redirect.visits, 0)

            self.assertEqual(
                redirect.destination,
                self.urls[i],
                f"Expected {self.urls[i]} - got {redirect.destination}"
            )

            self.assertEqual(
                redirect.id,
                id_encoder.debase_and_decode(redirect.code)
            )
