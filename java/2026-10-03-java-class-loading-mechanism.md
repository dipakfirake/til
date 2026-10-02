# Java Class Loading Mechanism

> _2026-10-03_ | Category: **java**

How JVM loads classes on demand.

```
ClassLoader Hierarchy:
┌───────────────────┐
│ Bootstrap Loader  │ ← java.lang, java.util (rt.jar)
├───────────────────┤
│ Extension Loader  │ ← javax.*, ext directory
├───────────────────┤
│ Application Loader│ ← classpath (your code)
├───────────────────┤
│ Custom Loaders    │ ← plugins, hot-reload
└───────────────────┘
```

```java
// Check which classloader loaded a class
System.out.println(String.class.getClassLoader());      // null (Bootstrap)
System.out.println(MyClass.class.getClassLoader());     // AppClassLoader

// Custom classloader for plugins
ClassLoader loader = new URLClassLoader(new URL[]{pluginJar});
Class<?> cls = loader.loadClass("com.plugin.MyPlugin");
Object plugin = cls.getDeclaredConstructor().newInstance();
```

**Delegation**: Child asks parent first → loads only if parent can't.
**Key Takeaway**: Understanding classloading helps debug `ClassNotFoundException` and `NoClassDefFoundError`.
