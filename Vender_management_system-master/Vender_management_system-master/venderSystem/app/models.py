from django.db.models import F
from django.db import models
from django.contrib.postgres.fields import JSONField
from django.db.models import Count, Avg
from django.db.models.functions import TruncDate
from django.db.models import ExpressionWrapper, fields

class Vendor(models.Model):
    name = models.CharField(max_length=255)
    contact_details = models.TextField()
    address = models.TextField()
    vendor_code = models.CharField(max_length=50, unique=True, blank=True)
    on_time_delivery_rate = models.FloatField(null=True, blank=True)
    quality_rating_avg = models.FloatField(null=True, blank=True)
    average_response_time = models.FloatField(null=True, blank=True)
    fulfillment_rate = models.FloatField(null=True, blank=True)

    def update_metrics(self):
        self.calculate_on_time_delivery_rate()
        self.calculate_quality_rating_avg()
        self.calculate_average_response_time()
        self.calculate_fulfillment_rate()

    def calculate_on_time_delivery_rate(self):
        # completed_pos = self.purchaseorder.filter(status='completed')
        # total_completed_pos = completed_pos.count()
        # on_time_delivery_pos = completed_pos.filter(delivery_date__lte=models.F('acknowledgment_date'))
        # on_time_delivery_rate = on_time_delivery_pos.count() / total_completed_pos if total_completed_pos != 0 else 0
        # self.on_time_delivery_rate = on_time_delivery_rate
        completed_pos = self.purchaseorder.filter(status='completed')
        total_completed_pos = completed_pos.count()
        
        # Adding a check for delivery_date
        on_time_delivery_pos = completed_pos.filter(delivery_date__lte=F('acknowledgment_date'))
        on_time_delivery_rate = on_time_delivery_pos.count() / total_completed_pos if total_completed_pos != 0 else 0
        
        self.on_time_delivery_rate = on_time_delivery_rate

    def calculate_quality_rating_avg(self):
        completed_pos_with_rating = self.purchaseorder.filter(status='completed', quality_rating__isnull=False)
        quality_rating_avg = completed_pos_with_rating.aggregate(Avg('quality_rating'))['quality_rating__avg']
        self.quality_rating_avg = quality_rating_avg

    def calculate_average_response_time(self):
        completed_pos_with_acknowledgment = self.purchaseorder.filter(status='completed', acknowledgment_date__isnull=False)
        avg_response_time = completed_pos_with_acknowledgment.annotate(response_time=ExpressionWrapper(F('acknowledgment_date') - F('issue_date'), output_field=fields.DurationField())).aggregate(Avg('response_time'))['response_time__avg']
        self.average_response_time = avg_response_time.total_seconds() if avg_response_time is not None else None

    def calculate_fulfillment_rate(self):
        total_pos =self.purchaseorder.count()
        successful_pos = self.purchaseorder.filter(status='completed', quality_rating__isnull=True)
        fulfillment_rate = successful_pos.count() / total_pos if total_pos != 0 else 0
        self.fulfillment_rate = fulfillment_rate

    def __str__(self):
        return self.name


class PurchaseOrder(models.Model):
    po_number = models.CharField(max_length=50, unique=True)
    vendor = models.ForeignKey('Vendor', on_delete=models.CASCADE, related_name='purchaseorder')
    order_date = models.DateTimeField()
    delivery_date = models.DateTimeField()
    items = models.JSONField()
    quantity = models.IntegerField()
    status = models.CharField(max_length=50, null=True, blank=True)
    quality_rating = models.FloatField(null=True, blank=True)
    issue_date = models.DateTimeField()
    acknowledgment_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"PO {self.po_number} - {self.vendor.name}"