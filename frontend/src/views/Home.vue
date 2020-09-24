<template>
  <div class="home">
    <PostsCard />
    <PostsCard />
    <PostsCard />
    <PostsCard />
  </div>
</template>

<script>
import PostsCard from '@/components/common/PostsCard'

export default {
  name: 'Home',
  components: {
    PostsCard
  }
}
</script>
