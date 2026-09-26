# Cross-Site Request Forgery (CSRF)

> _2026-09-27_ | Category: **security**

Tricking users into taking unwanted actions.

User is logged into `bank.com`.
User visits malicious `hacker.com`.
`hacker.com` has a hidden form:
```html
<form action="http://bank.com/transfer" method="POST">
  <input type="hidden" name="to" value="hacker_account">
  <input type="hidden" name="amount" value="1000">
</form>
<script>document.forms[0].submit();</script>
```
Because the user is logged into the bank, the browser automatically attaches the bank session cookies!

**Prevention**:
1. **Anti-CSRF Tokens**: Server sends a unique random token. Form must include it. Hacker can't read it due to Same-Origin Policy.
2. **SameSite Cookie Attribute**: Set `SameSite=Lax` or `Strict` on session cookies. Modern browsers default to Lax!
