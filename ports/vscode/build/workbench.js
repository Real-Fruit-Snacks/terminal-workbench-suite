'use strict';

const { alpha, mix, lighten, darken } = require('./lib/color');

// Tokens → VS Code workbench colors. Layering rule (THEME-SPEC §2.2):
// higher ordinal = further from the page, in both modes. Accent appears
// only on signal: active tab, activity item, buttons, badges, links,
// selections, git/diff/error state.
function workbenchColors(t, isDark) {
  const transparent = '#00000000';
  const selection = alpha(t.accent, isDark ? 0.2 : 0.17);
  const selectionInactive = alpha(t.accent, isDark ? 0.1 : 0.085);
  const lineHighlight = alpha(t.accentAlt, 0.075);
  const listActive = alpha(t.accent, 0.105); // nav-active recipe, spec §2.4
  const focusRing = alpha(t.accent, 0.18);
  const findMatch = alpha(t.warm, 0.22); // text-highlight recipe
  const findOther = alpha(t.warm, 0.11);
  const dropTint = alpha(t.accent, 0.08);
  const hoverTint = alpha(t.accent, 0.08);
  const shadow = '#00000038'; // rgba(0,0,0,.22) — the one allowed shadow (spec §4)
  const buttonHover = lighten(t.accent, 0.08); // "hover lightens the accent"

  return {
    // ----- base
    focusBorder: focusRing,
    foreground: t.textNormal,
    disabledForeground: t.textFaint,
    'widget.shadow': shadow,
    'widget.border': t.border,
    'selection.background': selection,
    descriptionForeground: t.textMuted,
    errorForeground: t.red,
    'icon.foreground': t.textMuted,
    'sash.hoverBorder': t.borderStrong,

    // ----- text content
    'textLink.foreground': t.accentAlt,
    'textLink.activeForeground': isDark ? lighten(t.accentAlt, 0.15) : darken(t.accentAlt, 0.15),
    'textBlockQuote.background': alpha(t.accent, 0.07),
    'textBlockQuote.border': t.accent,
    'textCodeBlock.background': t.bg2,
    'textPreformat.foreground': t.textSoft,
    'textPreformat.background': t.bg2,
    'textSeparator.foreground': t.border,

    // ----- buttons & badges
    'button.background': t.accent,
    'button.foreground': t.textOnAccent,
    'button.hoverBackground': buttonHover,
    'button.border': transparent,
    'button.secondaryBackground': t.bg3,
    'button.secondaryForeground': t.textNormal,
    'button.secondaryHoverBackground': t.bg4,
    'badge.background': t.accent,
    'badge.foreground': t.textOnAccent,
    'progressBar.background': t.accent,

    // ----- inputs
    'input.background': t.bg2,
    'input.foreground': t.textNormal,
    'input.border': t.border,
    'input.placeholderForeground': t.textFaint,
    'inputOption.activeBackground': alpha(t.accent, 0.13), // tag recipe: 13% fill
    'inputOption.activeBorder': alpha(t.accent, 0.28), // tag recipe: 28% border
    'inputOption.activeForeground': t.textNormal,
    'inputValidation.errorBackground': mix(t.bg1, t.red, 0.09), // callout recipe
    'inputValidation.errorBorder': mix(t.border, t.red, 0.34),
    'inputValidation.errorForeground': t.textNormal,
    'inputValidation.warningBackground': mix(t.bg1, t.warm, 0.09),
    'inputValidation.warningBorder': mix(t.border, t.warm, 0.34),
    'inputValidation.warningForeground': t.textNormal,
    'inputValidation.infoBackground': mix(t.bg1, t.accentAlt, 0.09),
    'inputValidation.infoBorder': mix(t.border, t.accentAlt, 0.34),
    'inputValidation.infoForeground': t.textNormal,
    'checkbox.background': t.bg2,
    'checkbox.foreground': t.accent,
    'checkbox.border': t.border,
    'dropdown.background': t.bg2,
    'dropdown.listBackground': t.bg2,
    'dropdown.foreground': t.textNormal,
    'dropdown.border': t.border,

    // ----- scrollbar (spec §5: transparent track, inset thumb from text-faint)
    'scrollbar.shadow': transparent,
    'scrollbarSlider.background': alpha(t.textFaint, 0.28),
    'scrollbarSlider.hoverBackground': alpha(t.textFaint, 0.46),
    'scrollbarSlider.activeBackground': alpha(t.textFaint, 0.6),

    // ----- lists & trees
    'list.activeSelectionBackground': listActive,
    'list.inactiveSelectionBackground': alpha(t.accent, 0.06),
    'list.hoverBackground': t.bg3,
    'list.focusBackground': listActive,
    'list.focusOutline': transparent,
    'list.dropBackground': dropTint,
    'list.highlightForeground': t.accentAlt,
    'list.focusHighlightForeground': t.accentAlt,
    'list.errorForeground': t.red,
    'list.warningForeground': t.warm,
    'list.deemphasizedForeground': t.textMuted,
    'listFilterWidget.background': t.bg2,
    'listFilterWidget.outline': t.border,
    'listFilterWidget.noMatchesOutline': t.red,
    'tree.indentGuidesStroke': t.border,

    // ----- toolbars
    'toolbar.hoverBackground': t.bg3,

    // ----- activity bar
    'activityBar.background': t.bg1,
    'activityBar.foreground': t.accent,
    'activityBar.inactiveForeground': t.textFaint,
    'activityBar.border': t.border,
    'activityBar.activeBorder': t.accent, // the 2px inset accent bar idiom
    'activityBar.activeBackground': listActive,
    'activityBarBadge.background': t.accent,
    'activityBarBadge.foreground': t.textOnAccent,

    // ----- side bar
    'sideBar.background': t.bg1,
    'sideBar.foreground': t.textSoft,
    'sideBar.border': t.border,
    'sideBarTitle.foreground': t.textMuted,
    'sideBarSectionHeader.background': t.bg1,
    'sideBarSectionHeader.foreground': t.textMuted,
    'sideBarSectionHeader.border': t.border,

    // ----- editor groups & tabs
    'editorGroup.border': t.border,
    'editorGroup.dropBackground': dropTint,
    'editorGroupHeader.tabsBackground': t.bg1,
    'editorGroupHeader.tabsBorder': t.border,
    'editorGroupHeader.noTabsBackground': t.bg1,
    'tab.activeBackground': t.bg3, // active pane idiom: bg-3 fill + accent label
    'tab.activeForeground': t.accent,
    'tab.activeBorderTop': t.accent,
    'tab.activeBorder': transparent,
    'tab.inactiveBackground': t.bg1,
    'tab.inactiveForeground': t.textMuted,
    'tab.hoverBackground': t.bg2,
    'tab.hoverForeground': t.textNormal,
    'tab.border': t.border,
    'tab.unfocusedActiveBackground': t.bg2,
    'tab.unfocusedActiveForeground': t.textSoft,
    'tab.unfocusedActiveBorderTop': alpha(t.accent, 0.4),
    'tab.unfocusedInactiveForeground': t.textFaint,

    // ----- editor core
    'editor.background': t.bg0,
    'editor.foreground': t.textSoft, // code default = text-soft (spec §2.3)
    'editorLineNumber.foreground': t.textFaint,
    'editorLineNumber.activeForeground': t.textMuted,
    'editorCursor.foreground': t.accent,
    'editor.selectionBackground': selection,
    'editor.inactiveSelectionBackground': selectionInactive,
    'editor.selectionHighlightBackground': alpha(t.accentAlt, 0.1),
    'editor.wordHighlightBackground': alpha(t.accentAlt, 0.09),
    'editor.wordHighlightStrongBackground': alpha(t.accent, 0.11),
    'editor.findMatchBackground': findMatch,
    'editor.findMatchBorder': t.warm,
    'editor.findMatchHighlightBackground': findOther,
    'editor.hoverHighlightBackground': alpha(t.accentAlt, 0.08),
    'editor.lineHighlightBackground': lineHighlight,
    'editor.lineHighlightBorder': transparent,
    'editor.rangeHighlightBackground': alpha(t.accent, 0.05),
    'editor.foldBackground': alpha(t.accentAlt, 0.05),
    'editorLink.activeForeground': t.accentAlt,
    'editorWhitespace.foreground': alpha(t.textFaint, 0.4),
    'editorIndentGuide.background1': t.border,
    'editorIndentGuide.activeBackground1': t.borderStrong,
    'editorRuler.foreground': t.border,
    'editorCodeLens.foreground': t.textFaint,
    'editorBracketMatch.background': alpha(t.accentAlt, 0.1),
    'editorBracketMatch.border': t.borderStrong,
    'editorBracketHighlight.foreground1': t.textSoft,
    'editorBracketHighlight.foreground2': t.accentAlt,
    'editorBracketHighlight.foreground3': t.warm,
    'editorBracketHighlight.foreground4': t.textSoft,
    'editorBracketHighlight.foreground5': t.accentAlt,
    'editorBracketHighlight.foreground6': t.warm,
    'editorBracketHighlight.unexpectedBracket.foreground': t.red,
    'editorInlayHint.background': alpha(t.textFaint, 0.1),
    'editorInlayHint.foreground': t.textFaint,
    'editorGhostText.foreground': t.textFaint,
    'editorStickyScroll.background': t.bg0,
    'editorStickyScrollHover.background': t.bg2,

    // ----- gutter & diff
    'editorGutter.background': t.bg0,
    'editorGutter.addedBackground': alpha(t.accent, 0.6),
    'editorGutter.modifiedBackground': alpha(t.accentAlt, 0.6),
    'editorGutter.deletedBackground': alpha(t.red, 0.6),
    'diffEditor.insertedTextBackground': alpha(t.accent, 0.12),
    'diffEditor.removedTextBackground': alpha(t.red, 0.12),
    'diffEditor.insertedLineBackground': alpha(t.accent, 0.07),
    'diffEditor.removedLineBackground': alpha(t.red, 0.07),
    'diffEditor.border': t.border,

    // ----- overview ruler & minimap
    'editorOverviewRuler.border': transparent,
    'editorOverviewRuler.findMatchForeground': alpha(t.warm, 0.6),
    'editorOverviewRuler.errorForeground': t.red,
    'editorOverviewRuler.warningForeground': t.warm,
    'editorOverviewRuler.infoForeground': t.accentAlt,
    'editorOverviewRuler.modifiedForeground': alpha(t.accentAlt, 0.6),
    'editorOverviewRuler.addedForeground': alpha(t.accent, 0.6),
    'editorOverviewRuler.deletedForeground': alpha(t.red, 0.6),
    'editorOverviewRuler.bracketMatchForeground': t.borderStrong,
    'minimap.background': t.bg0,
    'minimap.selectionHighlight': selection,
    'minimap.findMatchHighlight': alpha(t.warm, 0.4),
    'minimap.errorHighlight': alpha(t.red, 0.5),
    'minimap.warningHighlight': alpha(t.warm, 0.5),
    'minimapGutter.addedBackground': alpha(t.accent, 0.6),
    'minimapGutter.modifiedBackground': alpha(t.accentAlt, 0.6),
    'minimapGutter.deletedBackground': alpha(t.red, 0.6),

    // ----- diagnostics
    'editorError.foreground': t.red,
    'editorWarning.foreground': t.warm,
    'editorInfo.foreground': t.accentAlt,
    'editorHint.foreground': t.textFaint,
    'problemsErrorIcon.foreground': t.red,
    'problemsWarningIcon.foreground': t.warm,
    'problemsInfoIcon.foreground': t.accentAlt,

    // ----- editor widgets
    'editorWidget.background': t.bg2,
    'editorWidget.foreground': t.textNormal,
    'editorWidget.border': t.border,
    'editorSuggestWidget.background': t.bg2,
    'editorSuggestWidget.border': t.border,
    'editorSuggestWidget.foreground': t.textSoft,
    'editorSuggestWidget.highlightForeground': t.accentAlt,
    'editorSuggestWidget.focusHighlightForeground': t.accentAlt,
    'editorSuggestWidget.selectedBackground': listActive,
    'editorSuggestWidget.selectedForeground': t.textNormal,
    'editorHoverWidget.background': t.bg2,
    'editorHoverWidget.foreground': t.textSoft,
    'editorHoverWidget.border': t.border,
    'debugToolBar.background': t.bg2,
    'debugToolBar.border': t.border,

    // ----- peek view
    'peekView.border': t.accentAlt,
    'peekViewEditor.background': t.bg1,
    'peekViewEditor.matchHighlightBackground': findMatch,
    'peekViewResult.background': t.bg1,
    'peekViewResult.matchHighlightBackground': alpha(t.warm, 0.18),
    'peekViewResult.selectionBackground': listActive,
    'peekViewResult.fileForeground': t.textNormal,
    'peekViewResult.lineForeground': t.textMuted,
    'peekViewTitle.background': t.bg2,
    'peekViewTitleLabel.foreground': t.textNormal,
    'peekViewTitleDescription.foreground': isDark ? t.textMuted : t.textSoft,

    // ----- merge conflicts
    'merge.currentHeaderBackground': alpha(t.accent, 0.25),
    'merge.currentContentBackground': alpha(t.accent, 0.1),
    'merge.incomingHeaderBackground': alpha(t.accentAlt, 0.25),
    'merge.incomingContentBackground': alpha(t.accentAlt, 0.1),
    'merge.commonHeaderBackground': alpha(t.textFaint, 0.25),
    'merge.commonContentBackground': alpha(t.textFaint, 0.1),
    'editorOverviewRuler.currentContentForeground': t.accent,
    'editorOverviewRuler.incomingContentForeground': t.accentAlt,
    'editorOverviewRuler.commonContentForeground': t.textFaint,

    // ----- panel
    'panel.background': t.bg1,
    'panel.border': t.border,
    'panelTitle.activeForeground': t.accent,
    'panelTitle.activeBorder': t.accent,
    'panelTitle.inactiveForeground': t.textMuted,
    'panelSectionHeader.background': t.bg2,
    'panelSection.border': t.border,

    // ----- status bar (stays graphite — no default blue)
    'statusBar.background': t.bg1,
    'statusBar.foreground': t.textMuted,
    'statusBar.border': t.border,
    'statusBar.debuggingBackground': mix(t.bg1, t.warm, 0.15),
    'statusBar.debuggingForeground': t.textNormal,
    'statusBar.debuggingBorder': mix(t.border, t.warm, 0.34),
    'statusBar.noFolderBackground': t.bg1,
    'statusBar.focusBorder': focusRing,
    'statusBarItem.hoverBackground': hoverTint,
    'statusBarItem.activeBackground': alpha(t.accent, 0.12),
    'statusBarItem.prominentBackground': t.bg3,
    'statusBarItem.prominentForeground': t.textNormal,
    'statusBarItem.prominentHoverBackground': t.bg4,
    'statusBarItem.remoteBackground': alpha(t.accent, 0.13),
    'statusBarItem.remoteForeground': t.accent,
    'statusBarItem.errorBackground': mix(t.bg1, t.red, 0.15),
    'statusBarItem.errorForeground': t.red,
    'statusBarItem.warningBackground': mix(t.bg1, t.warm, 0.15),
    'statusBarItem.warningForeground': t.warm,

    // ----- title bar & command center
    'titleBar.activeBackground': t.bg1,
    'titleBar.activeForeground': t.textMuted,
    'titleBar.inactiveBackground': t.bg1,
    'titleBar.inactiveForeground': t.textFaint,
    'titleBar.border': t.border,
    'commandCenter.background': t.bg2,
    'commandCenter.foreground': isDark ? t.textMuted : t.textSoft,
    'commandCenter.activeBackground': t.bg3,
    'commandCenter.activeForeground': t.textNormal,
    'commandCenter.border': t.border,

    // ----- menus (float on bg-4 + the one allowed shadow)
    'menu.background': t.bg4,
    'menu.foreground': t.textNormal,
    'menu.border': t.border,
    'menu.selectionBackground': listActive, // accent tint — bg-3 would step backward from bg-4
    'menu.selectionForeground': t.textNormal,
    'menu.separatorBackground': t.border,
    'menubar.selectionBackground': t.bg3,
    'menubar.selectionForeground': t.textNormal,

    // ----- notifications (raised: bg-4)
    'notifications.background': t.bg4,
    'notifications.foreground': t.textNormal,
    'notifications.border': t.border,
    'notificationCenterHeader.background': t.bg3,
    'notificationCenterHeader.foreground': isDark ? t.textMuted : t.textSoft,
    'notificationToast.border': t.border,
    'notificationLink.foreground': t.accentAlt,
    'notificationsErrorIcon.foreground': t.red,
    'notificationsWarningIcon.foreground': t.warm,
    'notificationsInfoIcon.foreground': t.accentAlt,

    // ----- quick input / command palette
    'quickInput.background': t.bg2,
    'quickInput.foreground': t.textNormal,
    'quickInputTitle.background': t.bg3,
    'quickInputList.focusBackground': listActive,
    'quickInputList.focusForeground': t.textNormal,
    'pickerGroup.foreground': isDark ? t.textMuted : t.textSoft,
    'pickerGroup.border': t.border,
    'keybindingLabel.background': t.bg3,
    'keybindingLabel.foreground': t.textSoft,
    'keybindingLabel.border': t.border,
    'keybindingLabel.bottomBorder': t.borderStrong,

    // ----- breadcrumbs
    'breadcrumb.foreground': t.textMuted,
    'breadcrumb.background': t.bg0,
    'breadcrumb.focusForeground': t.textNormal,
    'breadcrumb.activeSelectionForeground': t.accent,
    'breadcrumbPicker.background': t.bg2,

    // ----- git decorations
    'gitDecoration.modifiedResourceForeground': t.accentAlt,
    'gitDecoration.addedResourceForeground': t.accent,
    'gitDecoration.untrackedResourceForeground': t.accent,
    'gitDecoration.renamedResourceForeground': t.accentAlt,
    'gitDecoration.deletedResourceForeground': t.red,
    'gitDecoration.ignoredResourceForeground': t.textFaint,
    'gitDecoration.conflictingResourceForeground': t.orange,
    'gitDecoration.stageModifiedResourceForeground': t.accentAlt,
    'gitDecoration.stageDeletedResourceForeground': t.red,

    // ----- debug
    'debugIcon.breakpointForeground': t.red,
    'debugIcon.breakpointDisabledForeground': t.textFaint,
    'debugIcon.startForeground': t.accent,
    'debugIcon.pauseForeground': t.warm,
    'debugIcon.stopForeground': t.red,
    'debugIcon.disconnectForeground': t.red,
    'debugIcon.restartForeground': t.accent,
    'debugIcon.stepOverForeground': t.accentAlt,
    'debugIcon.stepIntoForeground': t.accentAlt,
    'debugIcon.stepOutForeground': t.accentAlt,
    'debugIcon.continueForeground': t.accent,
    'debugIcon.stepBackForeground': t.accentAlt,
    'debugConsole.errorForeground': t.red,
    'debugConsole.warningForeground': t.warm,
    'debugConsole.infoForeground': t.accentAlt,
    'debugConsole.sourceForeground': t.textSoft,
    'debugConsoleInputIcon.foreground': t.accent,
    'debugTokenExpression.name': t.accentAlt,
    'debugTokenExpression.value': t.textSoft,
    'debugTokenExpression.string': t.accent,
    'debugTokenExpression.number': t.orange,
    'debugTokenExpression.boolean': t.orange,
    'debugTokenExpression.error': t.red,
    'editor.stackFrameHighlightBackground': alpha(t.warm, 0.15),
    'editor.focusedStackFrameHighlightBackground': alpha(t.accent, 0.12),

    // ----- settings ui
    'settings.headerForeground': t.textNormal,
    'settings.modifiedItemIndicator': t.accent,
    'settings.dropdownBackground': t.bg2,
    'settings.dropdownBorder': t.border,
    'settings.textInputBackground': t.bg2,
    'settings.textInputBorder': t.border,
    'settings.numberInputBackground': t.bg2,
    'settings.numberInputBorder': t.border,
    'settings.checkboxBackground': t.bg2,
    'settings.checkboxBorder': t.border,
    'settings.focusedRowBackground': alpha(t.accentAlt, 0.05),
    'settings.rowHoverBackground': alpha(t.accentAlt, 0.04),

    // ----- extensions view
    'extensionButton.prominentBackground': t.accent,
    'extensionButton.prominentForeground': t.textOnAccent,
    'extensionButton.prominentHoverBackground': buttonHover,
    'extensionBadge.remoteBackground': t.accent,
    'extensionBadge.remoteForeground': t.textOnAccent,
    'extensionIcon.starForeground': t.warm,
    'extensionIcon.verifiedForeground': t.accentAlt,

    // ----- welcome & walkthrough
    'welcomePage.background': t.bg0,
    'welcomePage.tileBackground': t.bg1,
    'welcomePage.tileHoverBackground': t.bg2,
    'welcomePage.progress.background': t.bg2,
    'welcomePage.progress.foreground': t.accent,
    'walkThrough.embeddedEditorBackground': t.bg1,

    // ----- banner & misc
    'banner.background': t.bg3,
    'banner.foreground': t.textNormal,
    'banner.iconForeground': t.accentAlt,
    'search.resultsInfoForeground': t.textMuted,
    'searchEditor.findMatchBackground': alpha(t.warm, 0.15),
    'editorMarkerNavigation.background': t.bg2,
    'editorMarkerNavigationError.background': t.red,
    'editorMarkerNavigationWarning.background': t.warm,
    'editorMarkerNavigationInfo.background': t.accentAlt,

    // ----- charts
    'charts.foreground': t.textNormal,
    'charts.lines': t.border,
    'charts.red': t.red,
    'charts.blue': t.ansiBlue,
    'charts.yellow': t.warm,
    'charts.orange': t.orange,
    'charts.green': t.accent,
    'charts.purple': t.violet,
  };
}

module.exports = { workbenchColors };
