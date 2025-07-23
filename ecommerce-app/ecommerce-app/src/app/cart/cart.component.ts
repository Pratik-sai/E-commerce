import { Component, OnInit } from '@angular/core';
import { CartService } from 'src/app/services/cart.service';
import { OrderService } from 'src/app/services/order.service';

@Component({
  selector: 'app-cart',
  templateUrl: './cart.component.html',
  styleUrls: ['./cart.component.css']
})
export class CartComponent implements OnInit {
  cartItems: any[] = [];
  totalAmount: number = 0;

  constructor(private cartService: CartService, private orderService: OrderService) { }

  ngOnInit(): void {
    this.loadCart();
  }

  loadCart() {
    this.cartService.getCartItems().subscribe(
      (response: any) => {
        this.cartItems = response.data;  // Make sure 'data' exists in your API response
        this.calculateTotalAmount();
      },
      (error) => {
        console.error('Error loading cart:', error);
      }
    );
  }

  calculateTotalAmount() {
    this.totalAmount = this.cartItems.reduce((sum, item) => sum + (item.amount * item.quantity), 0);
  }

  removeItem(cartItemId: number) {
    this.cartService.removeFromCart(cartItemId).subscribe(
      () => {
        this.cartItems = this.cartItems.filter(item => item.id !== cartItemId);
        this.calculateTotalAmount();
      },
      (error) => {
        console.error('Error removing item from cart:', error);
      }
    );
  }

  placeOrder() {
    const orderData = {
      cart_id: 1,  // Adjust this to get the actual cart ID if needed
      user: 'test_user',
      shipping_address: '123 Main St',
      total_amount: this.totalAmount
    };

    this.orderService.placeOrder(orderData).subscribe(
      (response: any) => {
        console.log('Order placed successfully:', response);
      },
      (error) => {
        console.error('Error placing order:', error);
      }
    );
  }
}
