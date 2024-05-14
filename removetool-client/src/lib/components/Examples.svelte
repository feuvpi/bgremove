<script>
  import { onMount } from 'svelte';
  import { createEventDispatcher } from 'svelte';
  import * as Carousel from "$lib/components/ui/carousel/index";
	import ImageSlider from './ImageSlider.svelte';
  import * as Tabs from "$lib/components/ui/tabs/index";

  
    let isMobile = false;
  
    // Check if the screen width is less than 640px (typical mobile breakpoint)
    const checkMobile = () => {
      isMobile = window.innerWidth < 640;
    };
  
    // Dispatch custom event when screen size changes
    const dispatch = createEventDispatcher();
  
    // Emit an event when the component mounts
    onMount(() => {
      checkMobile();
      dispatch('resize');
      window.addEventListener('resize', checkMobile);
      return () => {
        window.removeEventListener('resize', checkMobile);
      };
    });
  </script>
  

    {#if isMobile}
    <div class="flex flex-wrap">
    <Carousel.Root class="w-full max-w-xs">
        <Carousel.Content>
          {#each Array(5) as _, i (i)}
            <Carousel.Item>
              <!-- <div class="p-1">
                <Card.Root>
                  <Card.Content
                    class="flex aspect-square items-center justify-center p-6"
                  >
                    <span class="text-4xl font-semibold">{i + 1}</span>
                  </Card.Content>
                </Card.Root>
              </div> -->

              <ImageSlider/>
            </Carousel.Item>
          {/each}
        </Carousel.Content>
        <Carousel.Previous />
        <Carousel.Next />
      </Carousel.Root>
    </div>
    {:else}
      <!-- Render grid for normal screen -->
      <h2 class="text-center lg:mt-32 mt-18 font-sans text-4xl font-bold text-slate-800">Remove images backgrounds with ease</h2>

      <Tabs.Root value="animais" class="flex flex-col mt-4 mb-4 justify-center place-content-center items-center">
        <Tabs.List class="border-2 self-center grid w-full grid-cols-3 max-w-72">
          <Tabs.Trigger value="animais">Animais</Tabs.Trigger>
          <Tabs.Trigger value="pessoas">Pessoas</Tabs.Trigger>
          <Tabs.Trigger value="objetos">Objetos</Tabs.Trigger>
        </Tabs.List>
        <Tabs.Content value="animais">
        
      <div class="self-center flex max-w-7xl w-full flex-wrap mt-4 p-2 justify-center shadow-lg rounded-md">
        <div class="w-1/3 p-2 flex text-center justify-center ">
            <ImageSlider image1="/teste.png" image2="/FELV-cat.jpg" />
          </div>
          <div class="w-1/3 p-2  text-center justify-center ">
            <ImageSlider image1="/beijaflor-nobg.png" image2="/beijaflor.jpg" />
          </div>
          <div class="w-1/3 p-2  text-center justify-center ">
            <ImageSlider image1="/passaro-nobg.png" image2="/passaro.jpg" />
          </div>

      </div>
        </Tabs.Content>
        <Tabs.Content value="pessoas">
        
      <div class="self-center flex max-w-7xl w-full flex-wrap mt-4 p-2 border-2 justify-center shadow-lg rounded-md">
        <div class="w-1/3 p-2 flex text-center justify-center ">
            <ImageSlider image1="/teste.png" image2="/FELV-cat.jpg" />
          </div>
          <div class="w-1/3 p-2  text-center justify-center ">
            <ImageSlider image1="/beijaflor-nobg.png" image2="/beijaflor.jpg" />
          </div>
          <div class="w-1/3 p-2  text-center justify-center ">
            <ImageSlider image1="/passaro-nobg.png" image2="/passaro.jpg" />
          </div>

      </div>

        </Tabs.Content>

        <Tabs.Content value="objetos">
        
          <div class="self-center flex max-w-7xl w-full flex-wrap mt-4 p-2 border-2 justify-center shadow-lg rounded-md">
            <div class="w-1/3 p-2 flex text-center justify-center ">
              <ImageSlider image1="/passaro-nobg.png" image2="/passaro.jpg" />

              </div>
              <div class="w-1/3 p-2  text-center justify-center ">
                <ImageSlider image1="/beijaflor-nobg.png" image2="/beijaflor.jpg" />
              </div>
              <div class="w-1/3 p-2  text-center justify-center ">
                <ImageSlider image1="/teste.png" image2="/FELV-cat.jpg" />
              </div>
    
          </div>
    
            </Tabs.Content>
      </Tabs.Root>


    {/if}

  