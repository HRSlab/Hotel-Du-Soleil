<script lang="ts">
  import { onMount } from 'svelte';

  onMount(() => {
    const preventDefault = (e: Event) => {
      e.preventDefault();
      return false;
    };
    
    // Disable right click to prevent inspect and save image
    document.addEventListener('contextmenu', preventDefault);
    // Disable copy
    document.addEventListener('copy', preventDefault);
    // Disable dragging elements (like images/videos)
    document.addEventListener('dragstart', preventDefault);
    // Disable cutting
    document.addEventListener('cut', preventDefault);

    // Disable common DevTools shortcuts and printscreen
    const handleKeyDown = (e: KeyboardEvent) => {
      if (
        e.keyCode === 123 || // F12
        (e.ctrlKey && e.shiftKey && (e.keyCode === 73 || e.keyCode === 74 || e.keyCode === 67)) || // Ctrl+Shift+I/J/C (Windows DevTools)
        (e.ctrlKey && e.keyCode === 85) || // Ctrl+U (View Source)
        (e.metaKey && e.altKey && (e.keyCode === 73 || e.keyCode === 74 || e.keyCode === 67)) || // Cmd+Opt+I/J/C (Mac DevTools)
        (e.metaKey && e.altKey && e.keyCode === 85) || // Cmd+Opt+U (Mac View Source)
        (e.metaKey && e.shiftKey && (e.keyCode === 51 || e.keyCode === 52 || e.keyCode === 53)) || // Cmd+Shift+3/4/5 (Mac Screenshots)
        e.key === 'PrintScreen' // Windows Screenshot
      ) {
        e.preventDefault();
        return false;
      }
    };
    
    document.addEventListener('keydown', handleKeyDown);

    return () => {
      document.removeEventListener('contextmenu', preventDefault);
      document.removeEventListener('copy', preventDefault);
      document.removeEventListener('dragstart', preventDefault);
      document.removeEventListener('cut', preventDefault);
      document.removeEventListener('keydown', handleKeyDown);
    };
  });
</script>

<style>
  :global(:root) {
    /* Disable text selection */
    -webkit-user-select: none !important;
    -moz-user-select: none !important;
    -ms-user-select: none !important;
    user-select: none !important;
    /* iOS callout menu */
    -webkit-touch-callout: none !important;
  }
  
  :global(img), :global(video) {
    /* Disable pointer interactions to prevent right clicking on images */
    pointer-events: none !important;
    /* Extra drag protections */
    -webkit-user-drag: none !important;
    -khtml-user-drag: none !important;
    -moz-user-drag: none !important;
    -o-user-drag: none !important;
  }

  /* 
   * Allow clicking on links, buttons and inputs specifically 
   * since we disabled user-select and some pointer-events 
   */
  :global(a), :global(button), :global(input), :global(textarea), :global(select) {
    pointer-events: auto !important;
  }
  
  :global(a img), :global(button img) {
    /* For images inside links, we definitely don't want pointer events to hit the image */
    pointer-events: none !important;
  }
</style>
