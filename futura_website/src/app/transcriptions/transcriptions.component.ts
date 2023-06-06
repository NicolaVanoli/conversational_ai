import { identifierName } from '@angular/compiler';
import { Component, OnInit, Output } from '@angular/core';
import * as fs from 'fs';

import * as path from 'path';

@Component({

  selector: 'app-transcriptions',
  templateUrl: './transcriptions.component.html',
  styleUrls: ['./transcriptions.component.css']
})
export class TranscriptionsComponent implements OnInit {

  counter: number = 0;
  arr: object = [];

  constructor() {
  }

  ngOnInit(): void {
    // this.displayFiles();
    this.display_transcriptions();
  }



  display_transcriptions() {

    fetch("http://127.0.0.1:6655/transcriptions", { method: "GET" }).then(response => {
      if (response.status === 200) {
        return response.json();
      }
      else {
        throw new Error("HTTP status " + response.status);
      }
    })
      .then(json => {
        // console.log(JSON.stringify(json));
        let trNames = JSON.stringify(json);
        const myArray = trNames.split(",");
        this.arr = myArray;
        this.counter = myArray.length;
        this.create_buttons()
        // console.log(this.arr)

      }
      )
  }




  len_counter(i: number) {
    return new Array(i);
  }

  create_buttons() {
    let i = 1;
    // console.log(i)
    let body = document.getElementsByTagName("app-transcriptions")[0];
    let max = this.counter;
    for (i; i <= max; i++) {
      let button = document.createElement("button");
      button.innerHTML = Object.values(this.arr)[i - 1].replace('"', '').replace('.txt"', '').replace('[', '').replace(']', '').replace('tr_', '');
      button.classList.toggle('glow-on-hover');
      button.setAttribute('href', '#popup1');
      body.appendChild(button);
      button.addEventListener("click", function () {

        let id = this.innerHTML.replace('tr_', '');
        // console.log(id);
        get_transcription(id);
        myFunction();
      });

    }
  }




}

async function myFunction() {
  let box = document.getElementsByClassName('w3-modal')[0] as HTMLElement;
  box.style.display = 'block';
  box.style.position = 'fixed';
  box.style.visibility = 'visible';


}


async function get_transcription(id: string) {
  fetch("http://127.0.0.1:6655/open_transcription/" + id, { method: "PUT" })
    .then(response => {
      if (response.status === 200) {
        return Promise.resolve(response.json());
      }
      else {

        throw new Error("HTTP status " + response.status);
      }
    })
    .then(json => {
      let text = JSON.stringify(json);
      text = text.replace(/\\/g, ' ');
      text = text.replace(new RegExp('n","', "g"), '<br />').slice(2, -3);

      let container = document.getElementsByClassName('w3-container')[0] as HTMLElement;
      container.innerHTML = 'TRANSCRIPTION NUMBER: ' + id + '<br /><br />' + text;
      let sentButton = document.createElement("button");
      sentButton.innerHTML = 'Predict Sentiment';
      container.appendChild(sentButton);
      sentButton.addEventListener("click", function () {
        predictSentiment(id);
        // window.alert(typeof id);

      });
    }
    )

  // console.log(JSON.stringify(response.json()));

}

async function predictSentiment(id: string) {
  console.log(id);

  fetch("http://127.0.0.1:6655/predict_sentiment/" + id, { method: "PUT" })
    .then(response => {
      if (response.status === 200) {
        return Promise.resolve(response.json());
      }
      else {

        throw new Error("HTTP status " + response.status);
      }

    })
    .then(json =>
      // window.alert(json)
      // window.alert(JSON.stringify(json))
      generatePopup(json, () => {
        
        const popup = document.querySelector('.popup')
        popup!.parentNode!.removeChild(popup!)
      })
      );
}


function generatePopup(json: any[], action: () => void): void {
  // create the pop-up element
  let message = '';
  for (let element of json) {
    message+= element.replace('User:','') + '<br /><br />' ;
  }


  const popup = document.createElement('div');
  popup.classList.add('popup');
  popup.innerHTML = message;
  popup.style.position = 'absolute';
  popup.style.top = '0%';
  popup.style.left = '0%';
  popup.style.width = '5000px';
  popup.style.zIndex = '999';
  popup.style.height = '5000px';
  popup.style.fontSize = '3vmin';
  popup.style.overflow = 'scroll';
  popup.style.fontWeight = '100';
  popup.style.margin = 'auto';
  
  popup.style.backgroundColor = '#1abcb9';
  document.body.appendChild(popup);
  console.log(message);
  // add the click event listener to the pop-up element
  popup.addEventListener('click', action);
}