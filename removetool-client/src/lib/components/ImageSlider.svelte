<script lang="ts">
    export let image1 = '/teste.png';
    export let image2 = '/FELV-cat.jpg';
  
    let image1Style = '';
    let image2Style = '';
  
    let sliderValue = 0;
  
    $: {
      image1Style = `opacity: ${1 - sliderValue};`;
      image2Style = `opacity: ${sliderValue};`;
    }
  </script>

<!-- svelte-ignore a11y-missing-attribute -->
<div class="relative h-64 w-64 ">
    <!-- svelte-ignore a11y-missing-attribute -->
    <img
      class="absolute top-0 left-0 h-full w-full object-cover"
      src={image1}
      style={image1Style}
    />
    <img
      class="absolute top-0 left-0 h-full w-full object-cover"
      src={image2}
      style={image2Style}
    />
    <div class="absolute bottom-0 left-0 w-full h-2 bg-gray-300">
      <input
        type="range"
        min="0"
        max="1"
        step="0.01"
        bind:value={sliderValue}
        class=" Appearance-none w-full h-full cursor-pointer bg-transparent"
      />
    </div>
  </div>
  
  <style>
    input[type='range'] {
      --webkit-appearance: none;
      margin: 0;
      padding: 0;
      background-color: transparent;
    }
  
    input[type='range']::-webkit-slider-runnable-track {
      width: 100%;
      height: 8px;
      background-color: #ddd;
      border-radius: 1px;
      border: 0.2px solid #ccc;
      box-shadow: 0 1px 2px rgba(0, 0, 0, 0.4);
    }
  
    input[type='range']::-webkit-slider-thumb {
      -webkit-appearance: none;
      border: 0;
      height: 16px;
      width: 16px;
      border-radius: 50%;
      background-color: #4CAF50;
      margin-top: -4px;
    }
  </style>