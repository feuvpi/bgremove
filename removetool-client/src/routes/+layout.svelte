<script>
  import Header from './Header.svelte';
  import '../app.css';
  import Navbar from '$lib/components/Navbar.svelte';
	import Footer from '$lib/components/Footer.svelte';
</script>

<div class="min-h-screen flex flex-col">
  <Navbar class="sticky top-0 bg-gray-800 p-4 text-white" />

  <main class="flex-1 flex flex-col p-4 w-fit mx-auto mb-24">
    <slot />
  </main>
<Footer/>
  <footer class="flex justify-center items-center p-4">
    <p>Are you interested in buying this App? <a href="https://kit.svelte.dev" class="font-bold">Reach out</a> the developers.</p>
  </footer>
</div>