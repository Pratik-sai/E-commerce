import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { CartComponent } from './cart/cart.component';
import { OrderComponent } from './order/order.component';

const routes: Routes = [
  { path: 'cart', component: CartComponent },
  { path: 'orders', component: OrderComponent },
  { path: '', redirectTo: '/cart', pathMatch: 'full' }  // Default route to cart
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
