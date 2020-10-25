### git rebase Flow



2019-08-07

< git develop branch & rebase >

```
multicampus@DESKTOP-KVCQHCD MINGW64 ~/Desktop/project/hifive/team_HiFive/source (master)
$ git branch
* master

multicampus@DESKTOP-KVCQHCD MINGW64 ~/Desktop/project/hifive/team_HiFive/source (master)
$ git flow init -d
Using default branch names.

Which branch should be used for bringing forth production releases?
   - master
Branch name for production releases: [master]
Branch name for "next release" development: [develop]
Deletion of directory 'source' failed. Should I try again? (y/n) n


multicampus@DESKTOP-KVCQHCD MINGW64 ~/Desktop/project/hifive/team_HiFive/source (develop)
$ git branch
* develop
  master

multicampus@DESKTOP-KVCQHCD MINGW64 ~/Desktop/project/hifive/team_HiFive/source (develop)
$ git pull origin develop
remote: Enumerating objects: 12, done.
remote: Counting objects: 100% (12/12), done.
remote: Compressing objects: 100% (2/2), done.
remote: Total 7 (delta 5), reused 6 (delta 5), pack-reused 0
Unpacking objects: 100% (7/7), done.
From https://github.com/dkyou7/team_HiFive
 * branch            develop    -> FETCH_HEAD
   b11841b..b5165b7  develop    -> origin/develop
Updating b11841b..b5165b7
Fast-forward
 source/src/views/Header.vue | 2 +-
 1 file changed, 1 insertion(+), 1 deletion(-)

multicampus@DESKTOP-KVCQHCD MINGW64 ~/Desktop/project/hifive/team_HiFive/source (develop)
$ git checkout -b feature/header_add
Switched to a new branch 'feature/header_add'

multicampus@DESKTOP-KVCQHCD MINGW64 ~/Desktop/project/hifive/team_HiFive/source (feature/header_add)
$ git branch
  develop
* feature/header_add
  master

multicampus@DESKTOP-KVCQHCD MINGW64 ~/Desktop/project/hifive/team_HiFive/source (feature/header_add)
$ git status
On branch feature/header_add
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git checkout -- <file>..." to discard changes in working directory)

        modified:   src/views/Header.vue

no changes added to commit (use "git add" and/or "git commit -a")

multicampus@DESKTOP-KVCQHCD MINGW64 ~/Desktop/project/hifive/team_HiFive/source (feature/header_add)
$ git add -p
diff --git a/source/src/views/Header.vue b/source/src/views/Header.vue
index 13402b9..34902b5 100644
--- a/source/src/views/Header.vue
+++ b/source/src/views/Header.vue
@@ -1,6 +1,6 @@
 <template>
   <div class="Header">
-    this is header!
+    this is hifive
   </div>
 </template>

Stage this hunk [y,n,q,a,d,e,?]? y


multicampus@DESKTOP-KVCQHCD MINGW64 ~/Desktop/project/hifive/team_HiFive/source (feature/header_add)
$ git commit -m "[#6] header_add"
[feature/header_add 80f8847] [#6] header_add
 1 file changed, 1 insertion(+), 1 deletion(-)

multicampus@DESKTOP-KVCQHCD MINGW64 ~/Desktop/project/hifive/team_HiFive/source (feature/header_add)
$ git pull --rebase origin develop
From https://github.com/dkyou7/team_HiFive
 * branch            develop    -> FETCH_HEAD
Current branch feature/header_add is up to date.

multicampus@DESKTOP-KVCQHCD MINGW64 ~/Desktop/project/hifive/team_HiFive/source (feature/header_add)
$ git push origin feature/header_add
Enumerating objects: 11, done.
Counting objects: 100% (11/11), done.
Delta compression using up to 12 threads
Compressing objects: 100% (6/6), done.
Writing objects: 100% (6/6), 481 bytes | 240.00 KiB/s, done.
Total 6 (delta 5), reused 0 (delta 0)
remote: Resolving deltas: 100% (5/5), completed with 5 local objects.
remote:
remote: Create a pull request for 'feature/header_add' on GitHub by visiting:
remote:      https://github.com/dkyou7/team_HiFive/pull/new/feature/header_add
remote:
To https://github.com/dkyou7/team_HiFive.git
 * [new branch]      feature/header_add -> feature/header_add

multicampus@DESKTOP-KVCQHCD MINGW64 ~/Desktop/project/hifive/team_HiFive/source (feature/header_add)
$ git checkout develop
Switched to branch 'develop'
Your branch is up to date with 'origin/develop'.

multicampus@DESKTOP-KVCQHCD MINGW64 ~/Desktop/project/hifive/team_HiFive/source (develop)
$ git pull origin develop
remote: Enumerating objects: 1, done.
remote: Counting objects: 100% (1/1), done.
remote: Total 1 (delta 0), reused 0 (delta 0), pack-reused 0
Unpacking objects: 100% (1/1), done.
From https://github.com/dkyou7/team_HiFive
 * branch            develop    -> FETCH_HEAD
   b5165b7..da24ba1  develop    -> origin/develop
Updating b5165b7..da24ba1
Fast-forward
 source/src/views/Header.vue | 2 +-
 1 file changed, 1 insertion(+), 1 deletion(-)

multicampus@DESKTOP-KVCQHCD MINGW64 ~/Desktop/project/hifive/team_HiFive/source (develop)
$ git branch -D feature/header_add
Deleted branch feature/header_add (was 80f8847).

```

