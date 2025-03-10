from django.views.generic import TemplateView
from django.db.models import Sum
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render

from cafe.models import Order


class RevenueView(LoginRequiredMixin, TemplateView):
    template_name = "revenue.html"

    def get(self, request, *args, **kwargs):
        paid_orders = Order.objects.filter(status="paid")
        total_revenue = paid_orders.aggregate(
            Sum("total_price")
        )["total_price__sum"] or 0

        return render(request, self.template_name, {
            "orders": paid_orders,
            "total_revenue": total_revenue,
        })
