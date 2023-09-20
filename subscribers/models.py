from django.db import models
from django.utils import timezone


class Service(models.Model):
	service_name = models.CharField(max_length=30,unique=True)
	service_url = models.URLField(unique=True)
	active = models.BooleanField(default=True)
	created = models.DateField(default=timezone.now)
	updated = models.DateTimeField(auto_now=True)

	class Meta:
		ordering = ['-created',]

	@property
	def no_subscribers(self):
		numbers = Subscriber.objects.filter(service=self)
		return numbers.count()

	def __str__(self):
		return self.service_name


class Subscriber(models.Model):
	email = models.EmailField()
	service = models.ForeignKey(Service, on_delete=models.CASCADE)
	active = models.BooleanField(default=True)
	created = models.DateField(default=timezone.now)
	updated = models.DateTimeField(auto_now=True)

	class Meta:
		ordering = ['-created',]

	def __str__(self):
		return self.email


	class Meta:
		constraints = [
			models.UniqueConstraint(fields=['email', 'service'], name='unique_email_service')
		]
