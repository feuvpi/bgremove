<script lang="ts">
//@ts-nocheck

import { onMount } from 'svelte';

let dropArea; // Reference to the label element
let inputElement;
// Function to handle file selection
async function handleFile(files) {
  const file = files[0];
  // Do something with the file, for example:
  console.log('File selected:', file);

  const formData = new FormData();
  formData.append('file', file);

  try {
        const res = await fetch('http://127.0.0.1:5100', {
            method: 'POST',
            body: formData
        });

        if (res) {
            console.log('File uploaded successfully');

            const blob = await res.blob();

            // Create a URL for the blob
            const imageURL = URL.createObjectURL(blob);

            const link = document.createElement('a');
            link.href = imageURL;

// Set the download attribute to force download
link.setAttribute('download', 'nobg.png');

// Simulate a click on the link to trigger the download
link.click();

// Clean up by revoking the object URL
URL.revokeObjectURL(imageURL);

            // const img = new Image();
            // img.src = imageURL;

            
        } else {
            console.error('Failed to upload file:', res.statusText);
            // Handle the error if needed
        }
    } catch (error) {
        console.error('Error uploading file:', error);
        // Handle the error if needed
    }
  // If you want to preview the image, you can use FileReader
  const reader = new FileReader();
  reader.onload = function (e) {
    const img = new Image();
    img.src = e.target.result;
    img.onload = function () {
      // You can append the image to a container to display it
      // For example:
      // document.getElementById('preview-container').appendChild(img);
    };
  };
  reader.readAsDataURL(file);
}

// Function to handle drag over event
function handleDragOver(e) {
  e.preventDefault();
  e.currentTarget.classList.add('border-blue-500', 'border');
}

// Function to handle drag leave event
function handleDragLeave(e) {
  e.currentTarget.classList.remove('border-blue-500', 'border');
}

// Function to handle drop event
function handleDrop(e) {
  e.preventDefault();
  e.currentTarget.classList.remove('border-blue-500', 'border');
  const files = e.dataTransfer.files;
  if (files.length > 0) {
  handleFile(files);
  }
  
}

// Function to open file input dialog when the button is clicked
function openFileDialog() {
//   const inputElement = dropArea.querySelector('input[type=file]');
  inputElement.click();
}

// function handleInputChange(e){

// }



// Run the initialization logic when the component mounts
onMount(() => {
  dropArea = document.getElementById('drop');
  inputElement = dropArea.querySelector('input[type=file]');
  dropArea.addEventListener('dragover', handleDragOver);
  dropArea.addEventListener('dragleave', handleDragLeave);
  dropArea.addEventListener('drop', handleDrop);
  inputElement.addEventListener('change', function(event) {
        const files = event.target.files;
        if (files.length > 0) {
            // If files are selected, pass them to the handleFile function
            handleFile(files);
        }
    }, { once: true });
});
</script>


<section class="pt-20 md:pt-40">
    <div class="container mx-auto px-8 lg:flex">
        <div class="text-center lg:text-left lg:w-1/2">
            <img src="/cathero.png" alt="" class="relative w-48 border-2 border-emerald-500 top-100 w-40 rounded-full" />
            <h1 class="font-sans text-4xl lg:text-5xl xl:text-6xl font-bold leading-none">Remove Backgrounds from Images</h1>
            <p class="text-xl lg:text-2xl mt-6 font-medium font-sans">Quick, easy and free background removal tool.</p>

            <!-- <p class="mt-4 text-gray-600">Sed fermentum felis ut cursu</p> -->
        </div>
        <div class="lg:w-1/2">

            <div class="relative flex flex-col items-center mx-auto lg:flex-row-reverse lg:max-w-5xl lg:mt-8 xl:max-w-6xl">

                <!-- Image Column -->
                <div class="w-full h-64 lg:w-1/2 lg:h-auto">
                    <img class="h-full w-full object-cover" src="https://picsum.photos/id/1018/2000" alt="Winding mountain road">
                </div>
                <!-- Close Image Column -->
            
                <!-- Text Column -->

                <div class="md:max-w-2xl md:z-10 md:shadow-lg md:absolute md:top-0 md:mt-4 lg:w-3/5 lg:left-0 lg:mt-4 lg:ml-20 xl:mt-4 xl:ml-12 flex-1 items-center max-w-screen-sm mx-auto mb-3 space-y-4 sm:flex sm:space-y-0">
                    <div class="relative w-full">
                      <div class="items-center justify-center max-w-xl mx-auto">
                        
                        <label for="input" bind:this={dropArea} class="flex flex-col justify-center align-middle place-content-center w-80 h-72 px-4 transition bg-white border-2 border-gray-300 border-dashed rounded-md appearance-none cursor-pointer hover:border-gray-400 focus:outline-none" id="drop">
                            <button type="button" class="w-fit self-center place-self-center py-4 px-12 bg-teal-500 hover:bg-teal-600 rounded text-white mb-4" on:click={openFileDialog}>UPLOAD</button>
                            <div class="flex justify-center">
                                <svg xmlns="http://www.w3.org/2000/svg" class="w-6 h-6 text-gray-600" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
                                    <path stroke-linecap="round" stroke-linejoin="round" d="M7 16a4 4 0 01-.88-7.903A5 5 0 1115.9 6L16 6a5 5 0 011 9.9M15 13l-3-3m0 0l-3 3m3-3v12"></path>
                                </svg>
                                <span class="font-medium text-gray-600 ml-1">
                                    or drop a <span class="text-blue-600 underline ml-[4px]">image</span>
                                </span>
                            </div>
                            <input type="file" name="file_upload" class="hidden" accept="image/png,image/jpeg" id="input" onchange="handleFile(this.files)">
                        </label>
                      </div>
                    </div>
                  </div>

            </div>

        </div>
    </div>
</section>