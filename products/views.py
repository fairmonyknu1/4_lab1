from django.http import JsonResponse

def product_detail(request, productId):
    return JsonResponse({
        "id": str(productId),
        "name": f"{productId} name"
    })
