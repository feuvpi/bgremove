<script>
    import { onMount } from 'svelte';
    import { createEventDispatcher } from 'svelte';

// import * as Card from "$lib/components/ui/card/index.js";
import * as Carousel from "$lib/components/ui/carousel/index";
	import ImageSlider from './ImageSlider.svelte';
  
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
      <div class="flex flex-wrap mt-4 p-2 border-2 justify-centers shadow-lg rounded-md">
        <div class="w-1/3 p-2 ">
            <ImageSlider image1="/teste.png" image2="/FELV-cat.jpg" />
          </div>
          <div class="w-1/3 p-2">
            <ImageSlider image1="/beijaflor-nobg.png" image2="/beijaflor.jpg" />
          </div>
          <div class="w-1/3 p-2">
            <ImageSlider image1="/passaro-nobg.png" image2="/passaro.jpg" />
          </div>

      </div>

    {/if}

  