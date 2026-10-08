class PaymentService:
    @staticmethod
    def process_payment(payment):
        payment.payment_summary()
        payment.pay()