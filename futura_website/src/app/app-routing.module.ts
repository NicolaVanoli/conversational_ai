import { CommonModule } from '@angular/common';
import { NgModule } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { RouterModule, Routes } from '@angular/router';
import { AboutComponent } from './about/about.component';
import { HomeComponent } from './home/home.component';
import { TranscriptionsComponent } from './transcriptions/transcriptions.component';

const routes: Routes = [
  {path: "transcriptions", component: TranscriptionsComponent},
  {path: "home", component: HomeComponent},
  {path: "about", component: AboutComponent},
];

@NgModule({
  imports: [
    RouterModule.forRoot(routes),
    CommonModule,
    FormsModule,
  ],
  exports: [RouterModule]
})
export class AppRoutingModule { }
export class TranscriptionsModule{ }