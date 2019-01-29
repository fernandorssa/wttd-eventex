from django.core import mail
from django.test import TestCase


class SubscribePostValid(TestCase):
    def setUp(self):
        data = dict(name='Fernando Almeida', cpf='12345678901', email='fernando.rs.s.a@gmail.com', phone='48-99695-0459')
        self.client.post('/inscricao/', data)
        self.email = mail.outbox[0]

    def test_subscription_email_subject(self):
        expect = 'Confirmação de inscrição'

        self.assertEqual(expect, self.email.subject)

    def test_subscription_email_from(self):
        expect = 'contato@eventex.com.br'

        self.assertEqual(expect, self.email.from_email)

    def test_subscription_email_to(self):
        expect = ['contato@eventex.com.br', 'fernando.rs.s.a@gmail.com']

        self.assertEqual(expect, self.email.to)

    def test_subscription_email_body(self):
        contents = ['Fernando Almeida', '12345678901', 'fernando.rs.s.a@gmail.com', '48-99695-0459']
        for content in contents:
            with self.subTest():
                self.assertIn(content, self.email.body)
